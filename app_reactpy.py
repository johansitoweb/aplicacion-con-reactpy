from reactpy import component, html, run

@component
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    return html.div(
        html.h1(f"Contador: {count}"),
        html.button({"onClick": increment}, "Incrementar"),
        html.button({"onClick": decrement}, "Decrementar")
    )

run(counter)
