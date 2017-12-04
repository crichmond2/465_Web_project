$(function() {
	var scheme = window.location.protocol == "https:" ? "wss":"ws";
	var chatsock = new ReconnectingWebSocket(scheme + '://' + window.location.host + "/chat" + window.location.pathname);
	
	$('#charform').on('submit',function(event){
		var message = {
			handle: $('#handle').val(),
		        message: $('#message').val(),
	
		}
		chat_socket.send(JSON.stringify(message));
		return false;
	});
	chatsock.onmessage = function(message){
		var data = JSON.parse(message.data);
		$('#chat').append('<tr>'
			+ '<td>' + data.timestamp + '</td>'
			+ '<td>' + data.handle + '</td>'
			+ '<td>' + data.message + ' </td>'
			+ '</tr>');
	
	};
});	
