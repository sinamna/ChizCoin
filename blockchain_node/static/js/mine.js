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

            let modalCard=document.getElementById("mine-modal-card");
            let title=`<h4 class="card-title">${response['message']}</h4>`;
            let text= `<p class="card-text">
                        block Number:${response['block_number']}<br> nonce:${response['nonce']}`;
            modalCard.innerHTML+=title;
            modalCard.innerHTML+=text;
            $("#mineModal").modal('show')
            window.location.reload();
          },
          error: function(error){
            console.log(error);
          }
        });
      });

});