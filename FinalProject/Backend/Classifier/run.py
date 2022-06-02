from cProfile import label
import torch
from main import rnn,evaluate,lineToTensor,categoryFromOutput

labels ={
    0:"Knowledge",
    1:"Comprehension",
    2:"Synthesis",
    3:"Analysis",
    4:"Application",
    5:"Evaluation",
}


def predict(inp):
    line_tensor = lineToTensor(inp)
    output = evaluate(line_tensor)
    output = output.unsqueeze(0)
    # print(torch.argmax(output))
    guess = labels[int(torch.argmax(output))]
    print(f"Result: {guess}")
    return guess




if __name__ == "__main__":
    while True:
        rnn.hidden = rnn.init_hidden()
        s = input("Enter Que:")
        predict(s)


