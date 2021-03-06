import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = y.shape[0]

  scores = X @ W

  # normalize scores to maximum score be zero, it should increase numerical
  # stability
  scores -= np.max(scores, axis=1, keepdims=True)

  exp_scores = np.exp(scores)
  sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

  # Calculate probability of all classes (need for derevative)
  probs = exp_scores / sum_exp_scores

  # Calculate probability of correct classes
  correct_probs = probs[np.arange(num_train), y]

  # Calcualte loss and take mean from all samples
  loss = - np.log(correct_probs)
  loss = np.mean(loss)

  # Add regularization
  loss += 0.5*reg*np.sum(W * W)



  # calculus are easy in this case: predictions - hot_vector
  dscores = probs
  dscores[np.arange(num_train), y] -= 1
  dscores /= num_train

  # use backpropagation -> dimensional analyisis to get dW
  dW = X.T @ dscores

  # derivative of regularization
  dW += reg*W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################

  num_train = y.shape[0]

  scores = X @ W

  # normalize scores to maximum score be zero, it should increase numerical
  # stability
  scores -= np.max(scores, axis=1, keepdims=True)

  # Calculate intermediate values for probability
  exp_scores = np.exp(scores)
  sum_exp_scores = np.sum(np.exp(scores), axis=1, keepdims=True)

  # Calculate probability of all classes (need for derevative)
  probs = exp_scores / sum_exp_scores

  # Calculate probability of correct classes
  correct_probs = probs[np.arange(num_train), y]

  # Calcualte loss and take mean from all samples
  loss = - np.log(correct_probs)
  loss = np.mean(loss)

  # Add regularization
  loss += 0.5*reg*np.sum(W * W)



  # calculus are easy in this case: predictions - hot_vector
  dscores = probs
  dscores[np.arange(num_train), y] -= 1
  dscores /= num_train

  # use backpropagation -> dimensional analyisis to get dW
  dW = X.T @ dscores

  # derivative of regularization
  dW += reg*W




  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

