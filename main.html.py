<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FastAPI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
<header>
    <nav class="navar">
        <div class="p-3 mb-2 bg-primary text-white">
            <h1>CRUD Application</h1>
        </div>
    </nav>
</header>
<div class="container-fluid">
    {% block crud_container %}

    {% endblock %}
</div>
</body>
</html>