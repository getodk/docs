List of Available Methods
-----------------------------

.. list-table:: Available Methods
  :header-rows: 1

  * - | Method
    - Description
  * - | reigsterListener(listener)
    - Should be invoked once after registration and after all
      initialization is complete to ensure that any
      queued action is processed. 
  * - | hasListener()
    - Returns true if there is a listener already registered.
  * - | getPlatformInfo()
    - Returns the platform info as a stringified JSON object
      containing the keys: container, version, appName, baseUri, and logLevel.
  * - | getFileAsUrl(relativePath)
    - Take the path of a file relative to the app folder and return an absolute url
      by which it can be accessed.
  * - | getRowFileAsUrl(tableId, rowId, rowPathUri)
    - convert the rowpath value for a media attachment (e.g. uriFragment) field
      into a url by which it can be accessed.
  * - | lookupToken(stringToken)
    - Return the content of a display object for the given token. Note that this might
      include text, hint, image, etc. that are then localizable. In general, the resulting
      object can be customized further in survey XLSX files by specifying overrides for these
      fields.
  * - | getPreferredLocale()
    - Return an object representing the locale that was configured by the user in
      the Java-side's Device Settings
  * - | getLocaleDetails
    - Get an object containing details about the preferred locale (preferredLocale), whether
      the preferred locale is the same as the Device's locale (usingDeviceLocale), and other
      information about the device locale (isoCountry, displayCountry, isoLanguage, displayLanguage)
  * - | hasLocalization(locake, i18nToken)
    - Returns true if there is some type of localization for the given i18nToken and locale OR
      if there is a 'default' localization value. That localization might be any of: a text, 
      image, audio, or video element (i.e., the field name that can be localized is not specified).
  * - | hasFieldLocalization(locale, i18nToken, fieldName)
    - Returns true if there is some type of localization for the given fieldName in the given
      i18nToken and locale.
  * - | localizeTokenField(locale, i18nToken, fieldName)
    - Returns the localization for a given fieldName in a given i18nToken and locale.
  * - | localizeUrl(locale, i18nToken, fieldName, formPath)
    - Returns the localization for a given fieldName in a given i18nToken and locale and prefixes
      it with the given formPath if the url is not already prefixed with a slash or http prefix.
  * - | toDateFromOdkTimeStamp(timestamp)
    - | Convert an ODK Timestamp string to a Javascript Date() object. The ODK Timestamp string 
        is used to represent dateTime and date values. It is an iso8601-style UTC date
        extended to nanosecond precision: yyyy-mm-ddTHH:MM:SS.sssssssss. 
      | 
      | This value is assumed 
        to be UTC and the value is assumed to be in the AD calendar (no BC dates please!).
        'date' types use T00:00:00.000000000 for the time portion of the timestamp.
      |  
      | NOTE: This method discards the nano fields.
  * - | toDateFromOdkTime(refJsDate, time)
    - | This conversion takes an incoming 'refJsDate' Date() object, retrieves the LOCAL TIME 
        ZONE year, month, day from that object, then CONSTRUCTS A NEW DATE OBJECT beginning 
        with that LOCAL TIME ZONE year, month, day and applying the time to that object and 
        returns the adjusted Date() object. The time is added to the zero hour, so that changes 
        in daylight savings and standard time do not affect the calculations (HH can reach 
        24 hr during "fall back" days). 
      |
      | Time is 00-24hr nanosecond-extended iso8601-style representation: HH:MM:SS.sssssssss. 
        NOTE: This method discards the nano fields.
  * - | toDateFromOdkTimeInterval(refJsDate, timeInterval)
    - | This conversion takes an incoming 'refJsDate' Date() object, then CONSTRUCTS A NEW DATE 
        OBJECT beginning with that UTC date and applying the +/- time interval to that object 
        and returns the adjusted Date() object. 
      | If the 'revJsDate' and 00:00:00.0000 for the 
        time portion, if a timeInterval is positive, this produces a Date() with the time-of-day 
        of the time interval.  I.e., this works correctly for the 'time' data type. 
      | 
      | The padded 
        precision of the hour allows representation of the full 9999 year AD calendar range 
        of time intervals. 
      | 
      | Time intervals are padded with leading zeros and are of the form: 
        HHHHHHHH:MM:SS.sssssssss OR HHHHHHHH:MM:SS.sssssssss-. The negative sign, if present, 
        is at the far right end.
  * - | padWithLeadingZeros(value, places)
    - | Returns a string after padding the indicated integer value with leading zeros so that 
        the string representation ends up with at least 'places' number of characters (more if 
        the value has more significant digits than that). 
      | 
      | Examples: padWithLeadingZeros(45, 4) => '0045'. padWithLeadingZeros(-45, 4) => '-0045'.
  * - | padWithLeadingSpaces(value, places)
    - | Returns a string after padding the indicated integer value with leading spaces so that 
        the string representation ends up with at least 'places' number of characters (more if 
        the value has more significant digits than that). Note the treatment of negative values!
      | 
      | Examples: padWithLeadingSpaces(0, 4) => '   0'. padWithLeadingSpaces(45, 4) => '  45'.
        padWithLeadingSpaces(-45, 4) => '-  45'.
  * - | toOdkTimeStampFromDate(jsDate)
    - | Converts a Javascript Date to an ODK Timestamp. See toDateFromOdkTimeStamp() for the 
        format of a timestamp. This zero-fills to extend the accuracy of the Javascript Date 
        object to nanosecond accuracy. 
      | The UTC values of the supplied Javascript dateTime
        object are used. This value is assumed to be UTC and the value is assumed to be in 
        the AD calendar (no BC dates please!). 
      | 
      | Values destined for 'date' types should set 
        the UTC time to all-zeros for the time portion of the timestamp.  Or adjust this 
        after-the-fact in their own code.
  * - | toOdkTimeFromDate(jsDate)
    - | Extract the LOCAL TIME of a Javascript Date object. Times are padded with leading zeros 
        and are 00-23hr form: HH:MM:SS.sssssssss. 
      | 
      | Time is extracted as the millisecond offset from 
        the start of the local day, and then converted to a string representation. This ensures 
        that changes in daylight savings time / standard time are properly handled and can result 
        in HH being 24 during "fall back" days.
  * - | toOdkTimeIntervalFromDate(refJsDate, newJsDate)
    - | Calculates the interval of time between two Javascript Date objects and returns an 
        OdkTimeInterval. 
      | 
      | Time intervals are padded with leading zeros and are of the form: 
        HHHHHHHH:MM:SS.sssssssss OR HHHHHHHH:MM:SS.sssssssss-. i.e., the negative sign, if present, 
        is at the far right end. 
      | 
      | This conversion computes (newJsDate - refJsDate). The padded 
        precision of the hour allows representation of the full 9999 year AD calendar range of 
        time intervals.
  * - | log(level, loggingString, detail)
    - Log messages using WebLogger. Levels are A, D, E, I, S, V, W. Given loggingString will 
      be logged with given detail added.
  * - | getActiveUser()
    - Get active user.
  * - | getProperty(propertyId)
    - Get device properties.
  * - | getBaseUrl()
    - Get the base url.
  * - | setSessionVariable(elementPath, jsonValue)
    - Store a persistent key-value. This lasts for the duration of this screen and is retained
      under screen rotations. Useful if browser cookies don't work.
  * - | getSessionVariable(elementPath)
    - Retrieve a persistent key-value. This lasts for the duration of this screen and is retained
      under screen rotations. Useful if browser cookies don't work.
  * - | genUUID()
    - Generate a globally unique id.
  * - | constructSurveyUri(tableId, formId, rowId, screenPath, elementKeyToValueMap)
    - Constructs a uri of the form "content://org.opendatakit.provider.forms/<appName>/<tableId>
      /<formId>/#instanceId=<rowId>&screenPath=<screenPath>" followed by "&<key>=<value>" for each
      key in the elementKeyToValueMap).
  * - | doAction(dispatchStruct, action, intentObject)
    - | Execute an action (intent call).
      | 
      | Information on parameters:
      | dispatchStruct: Can be anything -- holds reconstructive state for JS If this is null, 
        then the Javascript layer is not notified of the result of this action. It just 
        transparently happens and the webkit might reload as a result of the activity
        swapping out.
      | 
      | action: The intent. e.g., org.opendatakit.survey.activities.MediaCaptureImageActivity
      | 
      | intentObject: An object with the following structure:
      | {
      |    "uri" : intent.setData(value)
      |    "data" : intent.setData(value)  (preferred over "uri")
      |    "package" : intent.setPackage(value)
      |    "type" : intent.setType(value)
      |    "action" : intent.setAction(value)
      |    "category" : either a single string or a list of strings for intent.addCategory(item)
      |    "flags" : the integer code for the values to store
      |    "componentPackage" : If both package and activity are specified,
      |    "componentActivity" : will call intent.setComponent(new ComponentInfo(package, activity))
      |    "extras" : { key-value map describing extras bundle }
      | }
      | Within the extras, if a value is of the form: opendatakit-macro(name), then substitute 
        this with the result of getProperty(name). If the action begins with "org.opendatakit." 
        then we also add an "appName" property into the intent extras if it was not specified.
      |
      | Returns one of:
      |    "IGNORE"                -- there is already a pending action
      |    "JSONException"         -- something is wrong with the intentObject
      |    "OK"                    -- request issued
      |    "Application not found" -- could not find app to handle intent
      | 
      | If the request has been issued, and the dispatchStruct is not null then
        the javascript will be notified of the availability of a result via the
        registerListener callback. That callback should fetch the the results via
        odkCommon.viewFirstQueuedAction().
        And they are removed from the queue via
        odkCommon.removeFirstQueuedAction();
  * - | closeWindow(resultCode, keyValueBundle)
    - | Terminate the current webkit by calling:
      | 
      | activity.setResult(resultCode, intent);
      | finish();
      |
      | Where the intent's extras are set to the content of the keyValueBundle
      | 
      | resultCode === 0 -- RESULT_CANCELLED
      | resultCode === -1  -- RESULT_OK
      | any result code >= 1 is user-defined. Unclear the level of support
      | 
      | This will log errors but any errors will cause a RESULT_CANCELLED exit. 
        See the logs for what the error was.
  * - | viewFirstQueuedAction()
    - | Returns the oldest queued action outcome or Url change. Return null if there are none.
        The action remains queued until removeFirstQueuedAction is called.
      | 
      | The return value is either a structure:
      | {  
      |     dispatchStruct: dispatchStruct,
      |     action: refAction,
      |     jsonValue: 
      |     {
      |         status: resultCodeOfAction, // 0 === success
      |         result: JSON representation of Extras bundle from result intent
      |     }
      | }
      |
      | or, a string value beginning with #:
        "#urlhash"   (if the Java code wants the Javascript to take some action without a reload)
  * - | removeFirstQueuedAction()
    - Removes the first queued action.



