document.addEventListener("DOMContentLoaded", function () {
  var script = document.createElement("script");
  script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
  script.setAttribute("data-website-id", "6de76ee0-0882-4210-b4c2-9a62ec8adb4b");
  script.setAttribute("data-project-name", "ODK Docs");
  script.setAttribute("data-project-color", "#009ECC");
  script.setAttribute("data-project-logo", "https://getodk.org/assets/img/logo-square.jpg");
  script.setAttribute("data-button-hide", true);
  script.setAttribute("data-modal-title-ask-ai", "ODK Docs AI");
  script.setAttribute("data-modal-ask-ai-input-placeholder", "Ask a question about ODK...");
  script.setAttribute("data-modal-override-open-id", "custom-ask-ai-button");
  script.setAttribute("data-mcp-enabled", "enabled");
  script.setAttribute("data-mcp-server-url", "https://odk-docs.mcp.kapa.ai");
  script.setAttribute("data-mcp-button-hidden", "false");
  script.async = true;
  document.head.appendChild(script);
});