$(document).ready(()=>{
    $("#view-transactions-btn").click(()=>{
        node_url=document.getElementById("node_url").value;
        $.ajax({
            url:node_url+"chain",
            type:'GET',
            success:response=>{
                let transactions=[];
                index=1;
                const dateOptions={
                    year:"numeric",
                    month:"short",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit"
                };
                for(i=1;i<response.length;i++){
                    let chain =response.chain;
                    for(j=0;j<chain[i].transactions.length;j++){
                        let currentDate=new Date(chain[i].transactions.timestamp*1000);
                        let formattedDate=currentDate.toLocaleTimeString("en-us",dateOptions);
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
                $("#transactions_table").dataTable({
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
    });
});