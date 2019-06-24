const vscode = require("vscode");
const moment = require("moment");
const { date_formats, time_formats } = require("./formats.js");

const checkDateString = () => {
    const editor = vscode.window.activeTextEditor;
    const selectionRange = editor.selection;
    const selectedString = editor.document.getText(selectionRange);

    var validFormats = [];
    var noFittingFormat = false;

    var formatsToSelect = ["Date", "Time"];

    vscode.window
        .showQuickPick(["Date", "Time"], {
            placeHolder: "Do you need the format for a Date or a Time?"
        })
        .then(selectedFormat => {
            if (selectedFormat === "Date") {
                var check = false;
                for (var i in date_formats) {
                    check = moment(
                        selectedString,
                        date_formats[i],
                        true
                    ).isValid();
                    if (check) {
                        validFormats.push(date_formats[i]);
                    }
                }
            } else {
                var check = false;
                for (var i in time_formats) {
                    check = moment(
                        selectedString,
                        time_formats[i],
                        true
                    ).isValid();
                    if (check) {
                        validFormats.push(time_formats[i]);
                    }
                }
            }

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
        });
};

module.exports = { checkDateString };
