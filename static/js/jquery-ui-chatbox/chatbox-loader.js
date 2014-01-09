
function escapeHtml (unsafe) {
  return unsafe
    .replace (/&/g, "&amp;")
    .replace (/</g, "&lt;")
    .replace (/>/g, "&gt;")
    .replace (/"/g, "&quot;")
    .replace (/'/g, "&#039;");
}

/*
  document ready.
*/
$(document).ready(
  function() {
    /*
      declare gloabl box variable,
      so we can check if box is alreay open,
      when user click toggle button
    */
    var box = null;

    /*
      if box variable is null then we will create
      chat-box.
    */
    box = $("#chat_div").chatbox({
      /*
	unique id for chat box
      */
      id:"你",
      user:
      {
	key : "value"
      },
      /*
	Title for the chat box
      */
      title : "与博主聊聊",
      /*
	messageSend as name suggest,
	this will called when message sent.
	and for demo we have appended sent message to our log div.
      */
      messageSent : function(id, user, msg)
      {
	$("#log").append(id + " said: " + escapeHtml(msg) + "<br/>");
        $("#chat_div").chatbox("option", "boxManager").addMsg(id, msg);
      }
    });
    box.chatbox("option", "boxManager").hideContent();

    /*
      we are now adding click hanlder for 
      toggle button.
    */
    
    $("input[type='button']").click(
      function(event, ui)
      {
	box.chatbox("option", "boxManager").toggleBox();
      });
  });
