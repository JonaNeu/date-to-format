const vscode = require("vscode");
const dtf = require("./dateToFormat.js");

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    let disposable = vscode.commands.registerCommand(
        "extension.date-to-dateformat",
        function() {
            dtf.checkDateString();
        }
    );

    context.subscriptions.push(disposable);
}

exports.activate = activate;

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
