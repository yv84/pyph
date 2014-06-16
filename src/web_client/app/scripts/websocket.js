$(function() {
  var conn = null;
  function log(msg) {
    var control = $('#_log');
    control.html(control.html() + msg);
    control.scrollTop(control.scrollTop() + 999);
  }
  function connect() {
    disconnect();
    var wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')
    wsUri += window.location.hostname;
    wsUri += ':8765' // port
    wsUri +='/' // path
    console.log(wsUri)
    conn = new WebSocket(wsUri);
    log('Connecting...');
    console.log(conn)
    conn.onopen = function() {
      log('Connected.');
      update_ui();
    };
    conn.onmessage = function(e) {
      log(e.data); // Received
    };
    conn.onclose = function() {
      log('Disconnected.');
      conn = null;
      update_ui();
    };
  }
  function disconnect() {
    if (conn != null) {
      log('Disconnecting...');
      conn.close();
      conn = null;
      update_ui();
    }
  }
  function update_ui() {
    var msg = '';
    if (conn == null) {
      $('#status').text('disconnected');
      $('#connect').html('Connect');
    } else {
      $('#status').text('connected (' + conn.protocol + ')');
      $('#connect').html('Disconnect');
    }
  }
  $('#connect').click(function() {
    if (conn == null) {
      connect();
    } else {
      disconnect();
    }
    update_ui();
    return false;
  });

  $('#send_client').click(function() {
    var text = $('#text').val();
    console.log(conn)
    //log('c>: ' + text);
    conn.send('c>'+text);
    $('#text').val('').focus();
    return false;
  });

  $('#send_server').click(function() {
    var text = $('#text').val();
    console.log(conn)
    //log('s>: ' + text);
    conn.send('s>'+text);
    $('#text').val('').focus();
    return false;
  });
/*      $('#text').keyup(function(e) {
    if (e.keyCode === 13) {
      $('#send_server').click();
      return false;
    }
  });*/
});
