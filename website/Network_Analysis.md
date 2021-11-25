---
title: "Network Analysis"
date: 2021-11-24T16:46:57+01:00
draft: false
---
> Add plot in/out degree distribution
### Analysis of degree distributions

**Inward degree distribution:** We see a power-law distribution, which has a large majority of nodes with few in-going links, and few instances of nodes with large in-going degrees. We can explain this by noting that the main characters overwhelmingly have many ingoing links from more minor characters, without referencing those characters in return. While interacctions with main characters are significant for minor characters, they are insignificant in the storyline of the main-characters, leading to a one-sided relationship. Similarly, the power law defines that a network usually consists of a few hubs that most other nodes are connected to. The magnitude of nodes with 0 ingoing edges is reduced after discarding all nodes not in the GCC. However, we will observe many nodes with no ingoing edges.

**Outward degree distribution:** We here see a somewhat Poisson-like distribution. However, we notice some cases where some characters have no outgoing connections. These characters were not removed when creating the GCC as they must still have an ingoing-link connecting them to the giant component. More specifically, they are referenced by a more "central" character, without them referencing that character in return. This means that the vast majority of characters that are in the GCC have just one ingoing-link.