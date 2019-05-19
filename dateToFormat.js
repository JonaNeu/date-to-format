const vscode = require('vscode');
const moment = require('moment');


const checkDateString = (selectedString) => {
    // console.log(selectedString);

    var validFormats = [];

    var check = false;
    for(var i in formats){
        check = moment(selectedString, formats[i], true).isValid();
        if(check){
            // console.log('Valid');
            validFormats.push(formats[i]);
        } else {
            // console.log('Not Valid');
        }
    }
    // console.log(validFormats);

    const value = vscode.window.showQuickPick(['explorer', 'search', 'scm', 'debug', 'extensions'], { placeHolder: 'Select the view to show when opening a window.' })
    .then(() => console.log(value));

    const textEditor = vscode.window.activeTextEditor;

    textEditor.edit((builder) => {
        // todo: get the range of the selected text
        builder.replace(new vscode.Range(0,0,1,0), 'Just replaced');
    });

    




    // handle if array is empty

    // use quickpick to show options https://code.visualstudio.com/api/references/vscode-api#window.showQuickPick
}

// Todo: Add more formats
const formats = [
    'DD-MMM-YYYY', 
    'DD-MMM-YYYY HH:mm a',
    'DD-MM-YYYY'
];




exports.checkDateString = checkDateString;
