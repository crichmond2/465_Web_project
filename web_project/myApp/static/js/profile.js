function new_chat(){
  var link = '/'+document.getElementById('chat_link').innerHTML
  var Win = window.open(link,"chat_window","width=500,height=400")
  show_chats()
}
function get_chat(Link){
  var link = '/chat/'+Link
  var Win = window.open(link,"chat_window","width=500,height=400")
}
function show_chats(){
  document.getElementById('chats').innerHTML = 'You better Show';
}
