$(document).ready(()=>{
    //creating mempool table
    $.ajax({
        url:"/transactions/get",
        type:'GET',
        success:(response)=>{
            let transactions=[];
            let index=1;
            const mempool=response["transactions"];
            for(i=0;i<mempool.length;i++){
                trx=[index,mempool[i]["receiver_address"],
                    mempool[i]['sender_address'],
                    mempool[i]['amount']]
                transactions.push(trx);
                index++;
            };


            $("#mempool-table").dataTable({
                data:transactions,
                columns:[{title:"#"},
                         {title:"Receiver Address"},
                         {title:"Sender Address"},
                         {title:"Chiz Amount"}],
                columnDefs:[{targets:[1,2,3],
                            render:$.fn.dataTable.render.ellipsis(25)}]
            });
        },
        error:(error)=>{
            console.log(error);
        }
    });


    $("#mine_button").click(function () {

        $.ajax({
          url: "/mine/core",
          type: "GET",
          success: function(response){
            $("#success-form").show();
            $("#alert-div").addClass("alert-success");
            $("#mine_title").text(response["message"]);
            $("#block_index").val(response["block_number"]);
            $("#nonce").val(response["nonce"]);
            $("#mining_result").modal('show');
          },
          error: function(error){
            // let err=JSON.parse(xhr.responseText);
            $("#success-form").hide();
            $("#alert-div").hide();
            $("#alert-div").addClass("alert-danger");
            $("#mine_title").text("No transaction to mine");
            $("#mining_result").modal('show');
            console.log(error.message);
            
          }
        });
      });
      $("#refresh_btn").click(()=>{
        window.location.reload();
      })
});