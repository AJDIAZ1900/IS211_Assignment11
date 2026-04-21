from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

todo_list = []

html_template = """
<h1>To Do List</h1>

<table border="1">
<tr>
    <th>Task</th>
    <th>Email</th>
    <th>Priority</th>
</tr>
{% for item in todos %}
<tr>
    <td>{{ item.task }}</td>
    <td>{{ item.email }}</td>
    <td>{{ item.priority }}</td>
</tr>
{% endfor %}
</table>

<h2>Add New Item</h2>
<form action="/submit" method="POST">
    Task: <input type="text" name="task"><br>
    Email: <input type="text" name="email"><br>
    Priority:
    <select name="priority">
        <option>Low</option>
        <option>Medium</option>
        <option>High</option>
    </select><br>
    <input type="submit" value="Add To Do Item">
</form>

<form action="/clear" method="POST">
    <input type="submit" value="Clear">
</form>
"""

@app.route('/')
def home():
    return render_template_string(html_template, todos=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if "@" not in email:
        return redirect('/')

    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    todo_list.append({
        "task": task,
        "email": email,
        "priority": priority
    })

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    global todo_list
    todo_list = []
    return redirect('/')

if __name__ == '__main__':
    app.run()
