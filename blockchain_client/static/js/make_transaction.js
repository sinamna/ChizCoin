$(document).ready(()=>{
$("#generate_transactions").click(()=>{
    $.ajax({
        url:"/transactions/generate",
        type:"POST",
        dataType:"json",
        data:$("#transaction_form").serialize(),
        success:(response)=>{
            document.getElementById("confirm_sender_address").value=response["transaction"]["sender_address"];
            document.getElementById("confirm_receiver_address").value=response["transaction"]["receiver_address"];
            document.getElementById("confirm_amount").value=response["transaction"]["amount"];
            document.getElementById("confirm_signature").value=response["signature"];
            $("#baseModal").modal('show');
        },
        error:(error)=>{
            console.log(error);
        }
    });
});


$("#confirm-transaction_button").click(()=>{
    node_url=document.getElementById("node_url").value;
    $.ajax({
        url:node_url+"transactions/new",
        type:"POST",
        headers: {'Access-Control-Allow-Origin':'*'}, //node CORS
        dataType:'json',
        data:$("#confirm_transaction_form").serialize(),
        success:(response)=>{
            $("#transaction_form")[0].reset();
            $("#confirm_transaction_form")[0].reset();
            
            $("#sender_address").val("");
            $("#sender_private_key").val("");
            $("#receiver_address").val("");
            $("#amount").val("");

            $("#baseModal").modal('hide');
            $("#success_transaction_modal").modal('show');
        },
        error:(error)=>{
            console.log(error);
        }

    });
});
});