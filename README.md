# DATA

Used "IIT Bombay English-Hindi Corpus"

Anoop Kunchukuttan, Pratik Mehta, Pushpak Bhattacharyya. The IIT Bombay English-Hindi Parallel Corpus. Language Resources and Evaluation Conference. 2018. 

Download Link : http://www.cfilt.iitb.ac.in/iitb_parallel/


The Parallel Corpus contains 1.6 Million Sentences. This was enough to train a NMT model.


# PREPROCESSING

1.  English Data needed Cleaning, But Hindi Data was brilliant already.

2.  For Subword tokenization :  Google sentencePiece with BPE.



# TRAINING

1.  Used OpenNMT-py for preprocessing and training.

2.  Transformer Model ( "Attention is all you need" ) Used .  Link : https://arxiv.org/abs/1706.03762

3.  Most of the Hyperparameters were taken as it is from given paper.

4.  Ran for 50K epochs.  (Was not necessary, 30K will do Fine)


# PREDICTION

1.  OpenNMT has very efficient translation function implemented.

2.  After Translating, We had to Detokenize to Evaluate our predictions.

3.  I have uploaded my predictions. But, Other Data must be Downloaded from IITB.


# EVALUATION


Bleu-1  : 46.5

Bleu-2  : 21.1

Bleu-3  : 10.4

Bleu-4  : 5.2


Prediction Perplexity  ==  1.9157
