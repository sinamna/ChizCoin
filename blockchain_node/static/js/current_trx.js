$(document).ready(()=>{


    $.ajax({
        url:"/chain",
        type: "GET",
        success:(response)=>{
            let transactions=[];
            index=1;
            for(i=1;i<response.length;i++){
                let chain =response.chain;
                for(j=0;j<chain[i].transactions.length;j++){
                    const dateOptions={
                        year:"numeric",
                        month:"short",
                        day: "numeric",
                        hour: "2-digit",
                        minute: "2-digit"
                    };
                    let currentDate=new Date(chain[i].transactions.timestamp*1000);
                    let formattedDate=date.toLocaleTimeString("en-us",options);
                    const trx=chain[i].transactions[j];
                    transactions.push([
                            index,
                            trx["receiver_address"],
                            trx["sender_address"],
                            trx["amount"],
                            formattedDate,
                            chain[i]["index"]
                        ]
                    );
                    index++;
                };
            };
            $("#current-trx-table").dataTable({
                data:transactions,
                columns:[{title:"#"},
                        {title:"Receiver Address"},
                        {title:"Sender Address"},
                        {title:"Chiz Amount"},
                        {title:"timestamp"},
                        {title:"Block Id"}],
                    columnDefs: [ {targets: [1,2,3,4,5], render: $.fn.dataTable.render.ellipsis( 25 )}]
                } );
        },
        error:error=>{
            console.log(error);
        }

    });

    $("#refresh-blockchain-btn").click(()=>{


        $.ajax({
            url:"/nodes/resolve",
            type:"GET",
            success:response=>{
                window.location.reload();
            },
            error:error=>{
                console.log(error);
            }
        })
    })





});