let=("Hi Abhishek My work id is {} and i work as a {}")
id=("214354656")
work=("Software Developer")
print(let.format(id,work))

let=(f"Hi Abhishek My work id is {id} and i work as a {work}")
print(let)

let=(f"Hi Abhishek My work id is {{id}} and i work as a {{work}}")
print(let)