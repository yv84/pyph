websocket = () ->
  console.log('load websocket')
  conn = null

  log = (msg) ->
      # jQuery('<li/>', {
      #     class: "btn-success"
      #     text: msg
      # }).appendTo('#packet_log');
      $( "#packet_log" ).append(msg)

  connect = () ->
      disconnect();
      wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')
      wsUri += window.location.hostname;
      wsUri += ':8765' # port
      wsUri +='/' # path
      console.log(wsUri)
      conn = new WebSocket(wsUri)
      console.log(conn)
      conn.onopen = () ->
          update_ui()

      conn.onmessage = (e) ->
          log(e.data); # Received

      conn.onclose = () ->
          conn = null
          update_ui()

  disconnect = () ->
      if (conn != null)
          conn.close()
          conn = null
          update_ui()

  update_ui = () ->
    msg = ''
    if (conn == null)
        $('#status').text('disconnected')
        $('#connect').html('Connect')
    else
        $('#status').text('connected (' + conn.protocol + ')')
        $('#connect').html('Disconnect')


  $('#connect').on 'click', () ->
      console.log('button connect')
      if (conn == null)
          connect()
      else
          disconnect()
      update_ui()
      return false

  $('#send_client').on 'click', () ->
      text = $('#text').val()
      console.log(conn)
      #log('c>: ' + text);
      conn.send('c>'+text)
      $('#text').val('').focus()
      return false

  $('#send_server').on 'click', () ->
      text = $('#text').val()
      console.log(conn)
      #log('s>: ' + text);
      conn.send('s>'+text)
      $('#text').val('').focus()
      return false



#window.websocket = websocket
$(websocket);
