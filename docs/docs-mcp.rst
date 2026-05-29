ODK Docs MCP Server
===================

ODK provides a `Model Context Protocol (MCP) <https://modelcontextprotocol.io/docs/getting-started/intro>`_ server that helps you and your AI agents search ODK documentation, answer questions, troubleshoot issues, and build forms and workflows.

The MCP server is hosted at ``https://odk-docs.mcp.kapa.ai``. You can add this endpoint to any AI tool that supports MCP.

ChatGPT
-------
Requires Pro, Plus, Team, Enterprise, or Edu subscription.

#. Enable Developer Mode: :guilabel:`Settings` → :guilabel:`Apps` → :guilabel:`Advanced settings` → :guilabel:`Developer mode`.
#. Open `ChatGPT Apps settings <https://chatgpt.com/#settings/Connectors>`_.
#. Click on :guilabel:`Create app` next to Advanced settings and create an app.
#. Enter the name: ``ODK Docs`` and connection: ``https://odk-docs.mcp.kapa.ai``, then ``Create``.

Learn more in the `ChatGPT's Developer Mode docs <https://developers.openai.com/api/docs/guides/developer-mode>`_.

Claude Code
-----------

Run this command in your project directory:

  .. code-block:: txt

   claude mcp add --transport http odk-docs https://odk-docs.mcp.kapa.ai

Learn more in the `Claude's MCP docs <https://code.claude.com/docs/en/mcp>`_.

OpenCode
--------

Add to ``opencode.json`` in your project root.

   .. code-block:: json

    {
      "mcp": {
        "odk-docs": {
          "type": "remote",
          "url": "https://odk-docs.mcp.kapa.ai",
          "enabled": true
        }
      }
    }

Learn more in the `OpenCode's MCP docs <https://opencode.ai/docs/mcp-servers>`_.

Others
------

Any tool that supports MCP servers can connect using the following URL.

   .. code-block:: txt
    
    https://odk-docs.mcp.kapa.ai
