Using HTTP caching for efficient pipelines
==========================================

Introduction
------------

When creating a data processing pipeline, there are several API endpoints you may be making use of:

   * the submission-related OData `"data documents" </central-api-odata-endpoints/#data-document>`_,
   * the `submissions.csv </central-api-submission-management/#exporting-root-data-to-plain-csv>`_ endpoint,
   * the `submissions.csv.zip </central-api-submission-management/#exporting-form-submissions-to-csv>`_ endpoint,
   * or the `submissions </central-api-submission-management/#listing-all-submissions-on-a-form>`_ endpoint as an index entry point for retrieving `individual submissions </central-api-submission-management/#retrieving-submission-xml>`_.

You could, of course, download everything anew from these endpoints with every run of your pipeline.
However, this can be a lot of data (and, depending, may use up quite some server resources), while potentially no actual changes have taken place.
Ideally, we wouldn't download data that we already have. Moreover, if we could know that the data hasn't changed, we could avoid running the pipeline altogether.
Standardized in the HTTP protocol is a way to accomplish this through a mechanism called *cache revalidation*. It works as follows.

How does cache revalidation work?
---------------------------------

For many APIs in ODK Central, responses are tagged with a version identifier. This version identifier goes into a response header with name :code:`ETag`.
A client such as a web browser that, for instance, downloads :code:`submissions.csv`, will remember that version identifier — say ":code:`A`" — and saves it together with specifics of the requested URL, and the received response, to a cache.
Then, the next time it requests :code:`submissions.csv` from that same URL, the browser will add an :code:`If-None-Match` request header with that saved version identifier, ":code:`A`".

This effectively asks the server:
   
   "Give me :code:`submissions.csv`, but *only if* its current version on your side is something other than :code:`A`".

Such a request is called a *conditional request*.

If the version on the server side is indeed still :code:`A`, it will return an empty response with code :code:`304`, which means "Not Modified".
And then the browser knows it can reuse the :code:`submissions.csv` that it has saved in its cache.

But if the data on the serverside had changed since we downloaded version ":code:`A`", then the condition in the request header (:code:`If-None-Match: "A"`; "only if it doesn't match A") will be satisfied, and we get the :code:`submissions.csv` as we would normally — accompanied by an :code:`ETag` response header that tells us the new version.

Thus, all that's needed for a data pipeline that saves bandwidth and compute resources, is that we keep track of these versions - reading them from the :code:`ETag` response headers, and setting them in our :code:`If-None-Match` request headers.
How this is done differs by programming environment — but all HTTP libraries will have some way of reading and setting header values.


Example
-------

The following example is how one could do conditional requests from the command line, using :code:`curl` (this works from version :code:`7.68.0` upwards).
Various values in the below example are fictive — refer to the `API documentation </central-api>`_ to learn what goes where to make this work for your own ODK project.

.. code-block::
   :emphasize-lines: 7-9

   curl \
   --verbose \
   --compressed \
   --silent \
   --show-error \
   --user         'my-central-username:my-central-password' \
   --etag-save    submissions.csv.etag \
   --etag-compare submissions.csv.etag \
   --output       submissions.csv \
   https://my.odkserver/v1/projects/1/forms/myform/submissions.csv


Some diagnostic information will be in the output, among the lines should be two like this:

.. code-block::

   < HTTP/1.1 200 OK
   < ETag: W/"eventhash:e7db81a7a0882c3943c9ac34420f5893"

The server calculated a version, and put it in the :code:`ETag` response header. :code:`curl` then saved this version to the file :code:`submissions.csv.etag`, as specified with :code:`--etag-save`.

Now if we run the exact same command again, :code:`curl` will use that same file (as specified through :code:`--etag-compare`) to create an :code:`If-None-Match` header to make the request *conditional*.
If nothing changed on the server side in the meantime, then running the command again should feature this line in the output:

.. code-block::

   < HTTP/1.1 304 Not Modified

This indicates that the previously downloaded :code:`submissions.csv` file is still up-to-date with what the server has.
No submission data was sent to us! That saved us bandwidth and server processing capacity.

Furthermore, we also know that since nothing changed, we don't need to run the rest of our pipeline, whatever it may be.

However, had the server's data been changed in the meantime — say a submission was added — then we would have seen a :code:`200 OK` line instead,
and :code:`curl` would have updated both the :code:`submissions.csv` file (with the latest data from the server)
and the :code:`submissions.csv.etag` file (containing the new version identifier, which we can use in our *next* revalidation).

Conclusion
----------

In this article we've seen how we can use HTTP caching techniques to avoid generating, downloading and processing the same data over and over again.
