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

$.ajax({
    url:"/nodes/get",
    type:'GET',
    success:(response)=>{
        let node=""
        const nodes=response['nodes'];
        for(let i=0;i<nodes.length;i++){
            node= `<a href="http://${nodes[i]}" class="list-group-item list-group-item-action list-group-item-dark">${nodes[i]}</a>`
            document.getElementById("nodes_list").innerHTML+=node;
        }
    },
    error:(error)=>{
        console.log(error);
    }
});


});