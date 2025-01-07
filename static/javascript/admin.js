$(document).ready(function () {
    // 表を更新する関数
    function updateTable(data) {
        const tableBody = $("#dataTable tbody");
        tableBody.empty(); // 既存のデータをクリア

        data.forEach(item => {
            const row = `
                <tr>
                    <td>${item.id}</td>
                    <td>${item.name}</td>
                    <td>${item.age}</td>
                </tr>
            `;
            tableBody.append(row);
        });
    }

    // データ取得リクエスト
    function fetchData(filterName = "") {
        // AJAXリクエストをPromise形式で処理
        $.ajax({
            url: "/get_data",
            method: "GET",
            data: { filter_name: filterName },
        })
        .then(function (response) {
            // 正常にデータを取得した場合
            updateTable(response);
        })
        .catch(function (error) {
            // エラーが発生した場合
            console.error("データ取得中にエラーが発生しました:", error);
            alert("データの取得に失敗しました。サーバーを確認してください。");
        });
    }

    // 初回ロード時に全データを取得
    fetchData();

    // フィルタボタンが押されたときの処理
    $("#filterButton").on("click", function () {
        const filterName = $("#filterInput").val();
        fetchData(filterName);
    });
});
