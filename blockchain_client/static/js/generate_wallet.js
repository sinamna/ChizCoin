$(document).ready(()=>{
    $("input").click(()=>{
        $.ajax({
            url: "/wallet/new",
            type: "GET",
            success:(response)=>{
                document.getElementById("private_key").innerHTML=response['private_key'];
                document.getElementById("public_key").innerHTML=response['public_key'];
                document.getElementById("warning").style.display="block";
            },
            error:(error)=>{
                console.log(error)
            }
        });
    });
});
