websocket = () ->
  console.log('load websocket')
  conn = null

  # setup drop menu
  do add_li_in_drop_list = () ->
      jQuery('<li/>').appendTo('#connections>ul')
      jQuery('<a/>', {href: "#", text: "None"}).appendTo('#connections>ul>:last-child')
      jQuery('<li/>').appendTo('#connections>ul')
      jQuery('<a/>', {href: "#", text: "Waiting"}).appendTo('#connections>ul>:last-child')
      $('#connections>ul').find('>li').on 'click', () ->
              choice_conn($(this).text())
      $('#connections').on 'mouseenter', () ->
          $('#connections>ul').css({'display': 'block'})
      $('#connections').on 'mouseleave', () ->
          $('#connections>ul').css({'display': 'none'})

  log = (json_msg) ->
      msg = JSON.parse(json_msg)
      # list of gsconnections
      if msg.conn
          console.log(msg.conn)
          # <li><a href="#">Conn1</a></li>
          $('#connections>ul').find('li:gt(1)').remove()
          for _conn in msg.conn
              jQuery('<li/>').appendTo('#connections>ul')
              jQuery('<a/>', {href: "#", text: _conn}).appendTo('#connections>ul>:last-child')
          $('#connections>ul').find('>li').on 'click', () ->
                  choice_conn($(this).text())

      else if jQuery('#stop').text() == 'Stop '
          for ii in msg
              jQuery('<li/>', {
                  class: "btn-success",
                  text: ii}).prependTo('#packet_log')


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
          choice_conn()

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

  $('#stop').on 'click', () ->
      console.log(jQuery('#stop').text())
      if jQuery('#stop').text() == 'Stop '
          jQuery('#stop').text('Resume ')
          jQuery('<span/>', {class: "glyphicon glyphicon-play"}).appendTo('#stop')
      else if jQuery('#stop').text() == 'Resume '
          jQuery('#stop').text('Stop ')
          jQuery('<span/>', {class: "glyphicon glyphicon-stop"}).appendTo('#stop')

  $('#connect').on 'click', () ->
      console.log('button connect')
      if (conn == null)
          connect()
      else
          disconnect()
      update_ui()
      return false

  $('#clear').on 'click', () ->
      console.log('button clear')
      jQuery("#packet_log").empty()
      return false


  $('#send_client').on 'click', () ->
      text = $('#text').val()
      msg = JSON.stringify({'c':text})
      conn.send(msg)
      $('#text').val('').focus()
      return false

  $('#send_server').on 'click', () ->
      text = $('#text').val()
      msg = JSON.stringify({'s':text})
      conn.send(msg)
      $('#text').val('').focus()
      return false

  choice_conn = (_conn) ->
      if _conn == undefined
          _conn = 'None'
      jQuery('#connections>a').text(_conn)
      msg = JSON.stringify({'conn':_conn})
      conn.send(msg)
      return false

#window.websocket = websocket
$(websocket);
