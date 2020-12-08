$(document).ready(()=>{
$("#add_node_btn").click(()=>{
    let URL="/nodes/register";
    $.ajax({
        url:URL,
        type:"POST",
        dataType:"json",
        data:$("#node_form").serialize(),
        success:(response)=>{

            console.log(response);
            document.getElementById("node_urls").value="";
            window.location.reload();
        },
        error:(error)=>{
            console.log(error);
        }
    });
});
});