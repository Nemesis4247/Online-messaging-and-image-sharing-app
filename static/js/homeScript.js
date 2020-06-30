alert('its working')
console.log(window.location);
var loc = window.location;
var wsStart = 'ws://';
if (loc.protocol == 'https:'){
    wsStart = 'wss://';
}
var endpoint = wsStart + loc.host + loc.pathname;
var socket = new WebSocket(endpoint)

let msg_to = document.getElementById('id_To');
let msg_text = document.getElementById('id_Text');
let msg_photo = document.getElementById('id_photo');

socket.onmessage = (e) => {
  console.log('message', e.data);
  var msg = JSON.parse(e.data)
  console.log('msg', msg)
  let table = document.getElementById('id_table')
  // let tr_first = table.childNodes[0].innerHTML = 'jhaat';
  let other_phone = document.createTextNode(msg['To'])
  let text = document.createTextNode(msg['Text'])
  let x = document.createElement('IMG');
  x.setAttribute("src", "/media/profile/download.png");
  x.setAttribute("width", "70px");
  x.setAttribute("height", "70px");
  let td2 = document.createElement('TD')
  td2.appendChild(other_phone);
  td2.appendChild(text);
  // td2.style.margin-left = '0px';

  let td1 = document.createElement('TD');
  td1.appendChild(x)
  let tr = document.createElement('TR');
  tr.appendChild(td1);
  tr.appendChild(td2);
  table.insertBefore(tr, table.childNodes[0]);
  table.className = "table-striped" + " container";
  // let td_image = tr_first.firstChild

  // let td2 = document.createElement("H4").appendChild(other_phone)
  // let tr = document.createElement("TR");
  // tr.appendChild(td_image);
  // tr.appendChild(td2);
  // table.insertBefore(tr_first, table.childNodes[0]);
}
socket.onopen = (e) => {
  console.log('open', e)
  formElem.onsubmit = (event) => {
    event.preventDefault();
    let data = {
        'To' : msg_to.value,
        'Text' : msg_text.value,
        'photo' : msg_photo.value
    }
    socket.send(JSON.stringify(data))
  }
}
socket.onerror = (e) => {
  console.log('error', e)
}
socket.onclose = (e) => {
  console.log('close', e)
}
