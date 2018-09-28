def evaluate(results):
    """
    Visualization code to display results of various learners.
    
    inputs:
      - learners: a list of supervised learners
      - stats: a list of dictionaries of the statistic results from 'train_predict()'
      - accuracy: The score for the naive predictor
      - f1: The score for the naive predictor
    """
  
    # Create figure
    fig, ax = pl.subplots(2, 2, figsize = (11,7))

    # Constants
    bar_width = 0.3
    colors = ['#A00000','#00A0A0','#00A000']
    
    # Super loop to plot four panels of data
    for k, learner in enumerate(results.keys()):
        for j, metric in enumerate(['train_time', 'rmse_train', 'pred_time', 'rmse_test']):
            for i in np.arange(5):
                
                # Creative plot code
                ax[j//5, j%5].bar(i+k*bar_width, results[learner][i][metric], width = bar_width, color = colors[k])
                ax[j//5, j%5].set_xticks([0.45, 1.45, 2.45])
                ax[j//5, j%5].set_xticklabels(["1%", "10%", "100%"])
                ax[j//5, j%5].set_xlabel("Training Set Size")
                ax[j//5, j%5].set_xlim((-0.1, 3.0))
    
    # Add unique y-labels
    ax[0, 0].set_ylabel("Time (in seconds)")
    ax[0, 1].set_ylabel("RMSE")
    ax[1, 0].set_ylabel("Time (in seconds)")
    ax[1, 1].set_ylabel("RMSE")
    
    # Add titles
    ax[0, 0].set_title("Model Training")
    ax[0, 1].set_title("RMSE on Training Subset")
    ax[1, 0].set_title("Model Predicting")
    ax[1, 1].set_title("RMSE on Testing Set")
    
    # Set y-limits for score panels
    ax[0, 1].set_ylim((0, 6))
    ax[0, 2].set_ylim((0, 6))
    ax[1, 1].set_ylim((0, 6))
    ax[1, 2].set_ylim((0, 6))

    # Create patches for the legend
    patches = []
    for i, learner in enumerate(results.keys()):
        patches.append(mpatches.Patch(color = colors[i], label = learner))
    pl.legend(handles = patches, bbox_to_anchor = (-.80, 2.53), \
               loc = 'upper center', borderaxespad = 0., ncol = 3, fontsize = 'x-large')
    
    # Aesthetics
    pl.suptitle("Performance Metrics for Three Supervised Learning Models", fontsize = 16, y = 1.10)
    pl.tight_layout()
    pl.show()
    