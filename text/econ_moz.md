
<head>
    <link rel="stylesheet" href="../styles.css">
</head>



# Sentiment analysis of the mission statements

To gain individual level insights into the Mozambican economy, I apply a a class-based TF-IDF procedure ([BERTtopic](https://arxiv.org/abs/2203.05794)) to cluster word embeddings from the mission statements in the BDR3, i.e. the same publication that I use in the first two chapters to observe the ownership structure of Mozambican firms. Below are two dimensional topic representations of the tree most common entry types registered in the BDR3. I auto-translated the mission statements from portugese to english before I applied the sentiment analysis. 

## Visual representations (click on the arrows to view) :

<details> 
<summary> Associations (associacao) </summary>
<br>
 <iframe src= "../assets/bert_topics/intertopic_distance/associacao_topic.html" width="100%" height="900px"></iframe>
</details>

<details> 
<summary> Individual company (sociedade individual) </summary>
<br>
<iframe src="../assets/bert_topics/intertopic_distance/sociedade_individual_topic.html" width="100%" height="600px"></iframe>
</details>

<details> 
<summary> Private limited company (sociedade por quotas) </summary>
<br>
<iframe src="../assets/bert_topics/intertopic_distance/sociedade_por_quotas_topic.html" width="100%" height="600px"></iframe>
</details>



# Illustration 1: Sport and religious faith associations over time
To illustrate how topic modeling unveils about the mozambican society, consider the question what kind civil societies are present in the mozambican society. 
For simplicity, lets assume we are sport related clubs, as well as christian or muslim faith. The following graph plots the number of annually registered associations that mention one of these tree topic in their mission statement. 
The figure shows two trends. Did the number of annually registered sports clubs and christian communities increased over the last two decades. 
In contrast the formalization, i.e. documentation in the public bulletin, of muslim communities remains a stable low level through out the same period. The National Statistics Institute estimated that around 20 of mozambican citizens are Muslims.

<img class="markdown-image" src="../assets/bert_topics/football_christian_muslim.png" alt="football_christian_muslim.png">


## Illustration 2: The supply chain if fertilizer over space and time

If we link the sentiment of registered firms to national trade statics, we gain additional insights. In this example, we look import of fertilizer into Mozambique, as measured by the BACI trade dataset. BACI builds up on the United Nations Commodity Trade Statistics Database (UN Comtrade) and cross validated bilateral import and export statistics. The figure below plot with a linechart the imports of fertilizer. The bar chart lists the numbers of annually registered companies that trade or produce fertilizer according to their mission statement in Mozambique between 1985 and 2021.


The figure shows that fertilizer imports skyrocketed in 2008, while the number of domestic companies that trade with fertilizer remained relatively stable before 2010. After 2010, the number of companies that trade with fertilizer increased, but the imports of fertilizer decreased to the initial import level. 
 
<img class="markdown-image" src="../assets/baci_bdr/fertilizer.jpg" alt="fertilizer.jpg">







