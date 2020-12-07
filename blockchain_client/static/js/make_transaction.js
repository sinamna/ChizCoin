$(document).ready(()=>{
$("#generate_transaction").click(()=>{




    $.ajax({
        url:"/transactions/generate",
        type:"POST",
        dataType:"json",
        data:$("#transaction_form").serialize(),
        success:(response)=>{
            document.getElementById("confirm-sender-address").value=response["transaction"]["sender_address"];
            document.getElementById("confirm_receiver_address").value=response["transaction"]["receiver_address"];
            document.getElementById("confirm-amount").value=response["transaction"]["amount"];
            document.getElementById("confirm-signature").value=response["transaction"]["signature"];
            $("#baseModal").modal('show');
        },
        error:(error)=>{
            console.log(error);
        }



    })
})





})