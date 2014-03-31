/* Basic sample plugin inserting a feincms mediaFile into the CKEditor editing area.
*/

// Register the plugin with the editor.
// http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.plugins.html
CKEDITOR.plugins.add( 'feincms',
{
    // The plugin initialization logic goes inside this method.
    // http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.pluginDefinition.html#init
    init: function(editor)
    {
        // Define an editor command that inserts a feincms. 
        // http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.editor.html#addCommand
        editor.addCommand( 'insertMediaFile',
            {
                // Define a function that will be fired when the command is executed.
                // http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.commandDefinition.html#exec
                exec : function(editor)
                {
                    // Define your callback function
                    function insertMediaFile(imageUrl) {
                        // Insert the imageUrl into the document. Style represents some standard props.
                        // http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.editor.html#insertHtml
                        editor.insertHtml('<img src="/media/' + imageUrl + '" style="float:left;margin-right:10px;margin-bottom:10px;width:200px;" />');
                    }

                    var imageUrl;
                    window.dismissRelatedLookupPopup = function (win, chosenId) {
                        imageUrl = $(win.document.body).find('#_refkey_' + chosenId).val();
                        insertMediaFile(imageUrl);
                        var name = windowname_to_id(win.name);
                        var elem = document.getElementById(name);
                        if (elem) {
                            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                                elem.value += ',' + chosenId;
                            } else {
                                document.getElementById(name).value = chosenId;
                            }
                        }
                        win.close();
                    };
                    
                    var win = window.open('/admin/medialibrary/mediafile/?_popup=1', 'id_image', 'height=500,width=800,resizable=yes,scrollbars=yes');
                    win.focus();
                }
            });
        // Create a toolbar button that executes the plugin command. 
        // http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.ui.html#addButton
        editor.ui.addButton( 'feincms',
        {
            // Toolbar button tooltip.
            label: 'Insert MediaFile',
            // Reference to the plugin command name.
            command: 'insertMediaFile',
            // Button's icon file path.
            icon: this.path + 'images/mediaFile.png'
        } );
    }
} );
