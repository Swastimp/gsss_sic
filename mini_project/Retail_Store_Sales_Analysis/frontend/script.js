document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append('file', document.getElementById('file').files[0]);

    let res = await fetch('/analyze', {
        method: 'POST',
        body: formData
    });
    let data = await res.json();

    document.getElementById('results').innerHTML = `
        <h3> Analysis Completed</h3>
        <a href="${data.cleaned_file}" class="btn btn-success mt-2">Download Cleaned Data</a>
        <a href="${data.store_summary}" class="btn btn-info mt-2">Download Store Summary</a>
        <a href="${data.weekday_summary}" class="btn btn-warning mt-2">Download Weekday Summary</a>
    `;
});
