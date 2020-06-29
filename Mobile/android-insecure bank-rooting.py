import frida, sys
 
jscode = """
Java.perform(function () {
    var Activity = Java.use('com.android.insecurebankv2.PostLogin');
    Activity.doesSUexist.implementation = function(){
        console.log('Patch1 done!!!');
        return false
    };
 
    Activity.doesSuperuserApkExist.implementation = function(a){
        console.log('Patch2 done!!!');
        return false
    };
});
"""
 
process = frida.get_usb_device().attach('com.android.insecurebankv2')
script = process.create_script(jscode)
script.load()
sys.stdin.read()