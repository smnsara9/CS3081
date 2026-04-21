from logic import Symbol
rain = Symbol("Rain")
model = {"Rain": True}
print(rain.evaluate(model))