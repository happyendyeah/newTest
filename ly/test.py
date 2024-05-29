from transformers import BertTokenizer

def encode_decode(text, model_name=r'C:\Users\yeren\Desktop\model\bert'):
    # Initialize the tokenizer
    tokenizer = BertTokenizer.from_pretrained(model_name)
    
    # Encode the text
    encoded_input = tokenizer.encode(text, add_special_tokens=True)
    
    # Decode the encoded input back to text
    decoded_output = tokenizer.decode(encoded_input)
    
    return decoded_output

def main():
    # Input text
    text = "public class test {\n  void tryMinimizeExits(Node n, int exitType, String labelName) {\n\n    // Just an 'exit'.\n    if (matchingExitNode(n, exitType, labelName)) {\n      NodeUtil.removeChild(n.getParent(), n);\n      compiler.reportCodeChange();\n      return;\n    }\n\n    // Just an 'if'.\n    if (n.isIf()) {\n      Node ifBlock = n.getFirstChild().getNext();\n      tryMinimizeExits(ifBlock, exitType, labelName);\n      Node elseBlock = ifBlock.getNext();\n      if (elseBlock != null) {\n        tryMinimizeExits(elseBlock, exitType, labelName);\n      }\n      return;\n    }\n\n    // Just a 'try/catch/finally'.\n    if (n.isTry()) {\n      Node tryBlock = n.getFirstChild();\n      tryMinimizeExits(tryBlock, exitType, labelName);\n      Node allCatchNodes = NodeUtil.getCatchBlock(n);\n      if (NodeUtil.hasCatchHandler(allCatchNodes)) {\n        Preconditions.checkState(allCatchNodes.hasOneChild());\n        Node catchNode = allCatchNodes.getFirstChild();\n        Node catchCodeBlock = catchNode.getLastChild();\n        tryMinimizeExits(catchCodeBlock, exitType, labelName);\n      }\n      /* Don't try to minimize the exits of finally blocks, as this\n       * can cause problems if it changes the completion type of the finally\n       * block. See ECMA 262 Sections 8.9 & 12.14\n       */\n      if (NodeUtil.hasFinally(n)) {\n        Node finallyBlock = n.getLastChild();\n        tryMinimizeExits(finallyBlock, exitType, labelName);\n      }\n    }\n\n    // Just a 'label'.\n    if (n.isLabel()) {\n      Node labelBlock = n.getLastChild();\n      tryMinimizeExits(labelBlock, exitType, labelName);\n    }\n\n    // TODO(johnlenz): The last case of SWITCH statement?\n\n    // The rest assumes a block with at least one child, bail on anything else.\n    if (!n.isBlock() || n.getLastChild() == null) {\n      return;\n    }\n\n    // Multiple if-exits can be converted in a single pass.\n    // Convert \"if (blah) break;  if (blah2) break; other_stmt;\" to\n    // become \"if (blah); else { if (blah2); else { other_stmt; } }\"\n    // which will get converted to \"if (!blah && !blah2) { other_stmt; }\".\n    for (Node c : n.children()) {\n\n      // An 'if' block to process below.\n      if (c.isIf()) {\n        Node ifTree = c;\n        Node trueBlock, falseBlock;\n\n        // First, the true condition block.\n        trueBlock = ifTree.getFirstChild().getNext();\n        falseBlock = trueBlock.getNext();\n        tryMinimizeIfBlockExits(trueBlock, falseBlock,\n            ifTree, exitType, labelName);\n\n        // Now the else block.\n        // The if blocks may have changed, get them again.\n        trueBlock = ifTree.getFirstChild().getNext();\n        falseBlock = trueBlock.getNext();\n        if (falseBlock != null) {\n          tryMinimizeIfBlockExits(falseBlock, trueBlock,\n              ifTree, exitType, labelName);\n        }\n      }\n\n      if (c == n.getLastChild()) {\n        break;\n      }\n    }\n\n    // Now try to minimize the exits of the last child, if it is removed\n    // look at what has become the last child.\n    for (Node c = n.getLastChild(); c != null; c = n.getLastChild()) {\n      tryMinimizeExits(c, exitType, labelName);\n      // If the node is still the last child, we are done.\n      if (c == n.getLastChild()) {\n        break;\n      }\n    }\n  }\n}"
    
    # Encode and decode the text
    result = encode_decode(text)
    
    # Output the result
    print("Original Text: ", text)
    print("Encoded & Decoded Text: ", result)

if __name__ == '__main__':
    main()
