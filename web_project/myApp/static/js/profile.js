function new_chat(){
  var link = '/'+document.getElementById('chat_link').innerHTML
  var Win = window.open(link,"chat_window","width=500,height=400")
  show_chats()
}

function show_chats(){
  document.getElementById('chats').innerHTML = 'You better Show';
}
