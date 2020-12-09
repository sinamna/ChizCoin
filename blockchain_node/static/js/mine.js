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
                paging:false,
                scrollY:400,
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

});