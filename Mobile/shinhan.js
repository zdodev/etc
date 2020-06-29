Java.perform(function () {
    /*
    var Activity = Java.use('com.shinhan.spplatform.main.CommonBaseActivity');
    Activity.checkRooting.implementation = function(){
        console.log('CommonBaseActivity');
        console.log("onResume() got called! Let's call the original implementation");
        //this.checkRooting();
        this.v0 = 1
    };
    */
    /*
    var Activity1 = Java.use('com.shinhan.spplatform.main.SolWebActivity');
    Activity1.start.implementation = function(){
        //console.log('SolWebActivity');
        return false
    };
    */

    var Activity3 = Java.use('com.shinhan.spplatform.main.qd');
    Activity3.onClick.implementation = function(a, b) {
        console.log('onClick called');
    };
    
    /*
    var Activity2 = Java.use('com.shinhan.bank.customcomponent.CustomDialog');
    Activity2.show.overload('android.content.Context', 'java.lang.String', 'java.lang.String', 
        'java.lang.String', 'android.content.DialogInterface$OnClickListener', 'java.lang.String',
        'android.content.DialogInterface$OnClickListener', 'java.lang.String', 'android.content.DialogInterface$OnClickListener',
        'boolean', 'boolean', 'android.content.DialogInterface$OnDismissListener').implementation = function(
            args4, args5, args6, args7, args8, args9, args10, args11, args12, args13, args14, args15
        ){
            console.log('test');
            console.log('args4:', args4);
            console.log('args5:', args5);
            console.log('args6:', args6);
            console.log('args7:', args7);
            console.log('args8:', args8);
            console.log('args9:', args9);
            console.log('args10:', args10);
            console.log('args11:', args11);
            console.log('args12:', args12);
            console.log('args13:', args13);
            console.log('args14:', args14);
            console.log('args15:', args15);

            args5 = '루팅 우회'
            args6 = '루팅 우회'
            //args7 = 'Yes'
            args7 = 'Yes'
            args9 = 'No'
            this.show(args4, args5, args6, args7, args8, args9, args10, args11, args12, args13, args14, args15);
        
        return null
        //return false
    */
});