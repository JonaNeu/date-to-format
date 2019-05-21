const vscode = require("vscode");
const moment = require("moment");

const checkDateString = () => {
    const editor = vscode.window.activeTextEditor;
    const selectionRange = editor.selection;
    const selectedString = editor.document.getText(selectionRange);

    var validFormats = [];
    var noFittingFormat = false;

    var check = false;
    for (var i in formats) {
        check = moment(selectedString, formats[i], true).isValid();
        if (check) {
            validFormats.push(formats[i]);
        }
    }

    // no fitting format
    if (validFormats.length < 1) {
        noFittingFormat = true;
        validFormats.push("No fitting format found.");
    }

    vscode.window
        .showQuickPick(validFormats, {
            placeHolder: "Select your format."
        })
        .then(selectedFormat => {
            if (!noFittingFormat) {
                editor.edit(builder => {
                    builder.replace(editor.selection, selectedFormat);
                });
            }
        });
};

// dividers / |
const formats = [
    // javascript specifics
    "DD-MMM-YYYY",
    "DD-MMM-YYYY HH:mm a"
];

exports.checkDateString = checkDateString;
