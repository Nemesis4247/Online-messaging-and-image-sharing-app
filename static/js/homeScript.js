console.log(window.location);
var loc = window.location;
var wsStart = 'ws://';
if (loc.protocol == 'https:'){
    wsStart = 'wss://';
}
var endpoint = wsStart + loc.host + loc.pathname;
var socket = new ReconnectingWebSocket(endpoint)

let msg_to = document.getElementById('id_To');
let msg_text = document.getElementById('id_Text');
let msg_photo = document.getElementById('id_photo');
let phone = {{ phone }};
phone = phone.toString();


socket.onmessage = (e) => {
  console.log('message', e.data);
  var msg = JSON.parse(e.data)
  console.log('msg', msg)

  if ( msg['From']==phone || msg['To']==phone){
    //display msg
    let table = document.getElementById('id_table')
    let h4 = document.createElement('H4');
    let other_phone = document.createTextNode(msg['To'])
    let text = document.createTextNode(msg['Text'])
    let x = document.createElement('IMG');
    x.setAttribute("src", "/media/profile/download.png");
    x.setAttribute("width", "70px");
    x.setAttribute("height", "70px");
    let send_receive = document.createTextNode('sent : ');
    if(msg['To']==phone){
        send_receive = document.createTextNode('received : ');
        other_phone = document.createTextNode(msg['From'])
    }
    h4.appendChild(other_phone);
    let td2 = document.createElement('TD')
    td2.appendChild(h4);
    td2.appendChild(send_receive);
    td2.appendChild(text);

    let td1 = document.createElement('TD');
    td1.appendChild(x)
    let tr = document.createElement('TR');
    tr.appendChild(td1);
    tr.appendChild(td2);
    table.insertBefore(tr, table.childNodes[0]);
    table.className = "table-striped" + " container";


    //display received photo
    if (msg['photo']){
        let table_photo = document.getElementById('id_table_photo')
        let x_photo = document.createElement('IMG');
        x_photo.setAttribute("src", msg['photo']);
        x_photo.setAttribute("width", "300px");
        x_photo.setAttribute("height", "300px");

        let send_receive_photo = document.createTextNode('   sent to : ');
        let other_phone_photo = document.createTextNode(msg['To'])
        if(msg['To']==phone){
            send_receive_photo = document.createTextNode('   received from : ');
            let other_phone_photo = document.createTextNode(msg['From'])
        }
        let tr_photo = document.createElement('TR');
        let br_photo = document.createElement('BR');
        tr_photo.appendChild(x_photo)
        // tr_photo.appendChild(br_photo);
        tr_photo.appendChild(send_receive_photo)
        tr_photo.appendChild(other_phone_photo)
        table_photo.insertBefore(tr_photo, table_photo.childNodes[0]);
        table_photo.className = "table-striped" + " container";
    }
  }

}
socket.onopen = (e) => {
  console.log('open', e)
  formElem.onsubmit = async (event) => {
    event.preventDefault();
    let formData = new FormData(formElem)
    formData.append('From', {{ phone }})
    let response = await fetch('http://127.0.0.1:8000/send_message/', {
      method : 'POST',
      body : formData
    });
    let result = await response.json()
    let data = {
        'From' : phone,
        'To' : msg_to.value,
        'Text' : msg_text.value,
        'photo' : msg_photo.value
    }
    socket.send(JSON.stringify(data))
    form = document.getElementById('formElem');
    form.reset();
  }
}
socket.onerror = (e) => {
  console.log('error', e)
}
socket.onclose = (e) => {
  console.log('close', e)
}

//tabs functionality enabled
document.getElementById("defaultOpen").click();
function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
