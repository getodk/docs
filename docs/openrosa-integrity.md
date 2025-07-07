# Integrity API

This standard defines how clients can check the integrity of entity lists that are attached to forms as media files.

## Integrity request

Integrity requests can be made with an HTTP `GET` request to the server provided integrity URL with a comma-separated `id` query parameter specifying the ids of entities being checked. For example:

```
https://example.com/integrity?id=1,2,3
```

This request will return an integrity document.

### Integrity document

The structure of the integrity document returned by an integrity request is as follows:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<data>
<entities>
    <entity id="24b47424-ccf8-4f4b-b4cd-34ff5c71eddd">
        <deleted>true</deleted>
    </entity>
    <entity id="9e32d18f-d51a-4826-a8b2-e9b1c6d10b58">
        <deleted>false</deleted>
    </entity>
</entities>
</data>
```

This document consists of:

- A top-level `<data/>` tag in the `http://openrosa.org/xforms/xformsIntegrity` namespace enclosing:
  - zero or more `<entity/>` tags containing a exactly one `<deleted/>` tag

#### Elements with `<entity/>`

- `<deleted/>` should contain `true` if the entity has been deleted on the server, and `false` if not

#### `<entity/>` attributes

- `id`: id of the entity
