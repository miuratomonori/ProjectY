$(document).ready(function () {
    // 表を更新する関数
    function updateTable(data) {
        const tableBody = $("#dataTable tbody");
        tableBody.empty(); // 既存のデータをクリア

        data.forEach(item => {
            const row = `
                <tr>
                    <td>${item.name}</td>
                    <td>${item.student_id}</td>
                    <td>${item.registration_number}</td>
                    <td>${item.major}</td>
                    <td>${item.subject}</td>
                    <td>${item.attendance_count}</td>
                    <td>${item.absence_count}</td>
                </tr>
            `;
            tableBody.append(row);
        });
    }

    // データ取得リクエスト
    function fetchData(filters) {
        $.ajax({
            url: "/get_data",
            method: "GET",
            data: filters,
        })
        .then(function (response) {
            updateTable(response);
        })
        .catch(function (error) {
            console.error("データ取得中にエラーが発生しました:", error);
            alert("データの取得に失敗しました。");
        });
    }

    // フィルタボタンが押されたときの処理
    $("#filterButton").on("click", function () {
        const filters = {
            filter_name: $("#filterName").val(),
            filter_subject: $("#filterSubject").val(),
            filter_student_id: $("#filterStudentID").val(),
            filter_major: $("#filterMajor").val(),
        };
        fetchData(filters);
    });

    // 初回ロード時に全データを取得
    fetchData({});
});
