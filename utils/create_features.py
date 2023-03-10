from extract_features.actions_involving_impression_session import ActionsInvolvingImpressionSession
from extract_features.adjusted_location_reference_percentage_of_clickouts import AdjustedLocationReferencePercentageOfClickouts
from extract_features.adjusted_location_reference_percentage_of_interactions import AdjustedLocationReferencePercentageOfInteractions
from extract_features.adjusted_perc_click_per_impressions import AdjustedPercClickPerImpressions
from extract_features.platform_features_similarity import PlatformFeaturesSimilarity
from extract_features.adjusted_platform_reference_percentage_of_clickouts import AdjustedPlatformReferencePercentageOfClickouts
from extract_features.adjusted_platform_reference_percentage_of_interactions import AdjustedPlatformReferencePercentageOfInteractions
from extract_features.avg_price_interactions import AvgPriceInteractions
from extract_features.change_impression_order_position_in_session import ChangeImpressionOrderPositionInSession
from extract_features.changes_of_sort_order_before_current import ChangeOfSortOrderBeforeCurrent
from extract_features.city_session import CitySession
from extract_features.city_session_populars_only import CitySessionPopularsOnly
from extract_features.classifier_parro import ClassifierParro
from extract_features.classifier_piccio import ClassifierPiccio
from extract_features.country_searched_session import CountrySearchedSession
from extract_features.day_moment_in_day import DayOfWeekAndMomentInDay
from extract_features.fraction_pos_price import FractionPosPrice
from extract_features.frenzy_factor_consecutive_steps import FrenzyFactorSession
from extract_features.impression_features import ImpressionFeature
from extract_features.impression_position_in_percentage import ImpressionPositionInPercentage
from extract_features.impression_position_session import ImpressionPositionSession
from extract_features.impression_price_info_session import ImpressionPriceInfoSession
from extract_features.impression_rating import ImpressionRating
from extract_features.impression_rating_numeric import ImpressionRatingNumeric
from extract_features.impression_stars_numeric import ImpressionStarsNumeric
from extract_features.label import ImpressionLabel
from extract_features.last_clickout_filters_satisfaction import LastClickoutFiltersSatisfaction
from extract_features.last_steps_before_clickout import StepsBeforeLastClickout
from extract_features.lazy_user import LazyUser
from extract_features.location_features_similarity import LocationFeaturesSimilarity
from extract_features.location_reference_percentage_of_clickouts import LocationReferencePercentageOfClickouts
from extract_features.location_reference_percentage_of_interactions import LocationReferencePercentageOfInteractions
from extract_features.mean_price_clickout import MeanPriceClickout
from extract_features.normalized_platform_features_similarity import NormalizedPlatformFeaturesSimilarity
from extract_features.num_impressions_in_clickout import NumImpressionsInClickout
from extract_features.num_times_item_impressed import NumTimesItemImpressed
from extract_features.past_future_session_features import PastFutureSessionFeatures
from extract_features.perc_click_per_impressions import PercClickPerImpressions
from extract_features.perc_click_per_pos import PercClickPerPos
from extract_features.personalized_top_pop import PersonalizedTopPop
#from extract_features.platform_features_similarty import PlatformFeaturesSimilarity
from extract_features.platform_reference_percentage_of_clickouts import PlatformReferencePercentageOfClickouts
from extract_features.platform_reference_percentage_of_interactions import PlatformReferencePercentageOfInteractions
from extract_features.platform_session import PlatformSession
#from extract_features.price_info_session import PriceInfoSession
from extract_features.price_quality import PriceQuality
from extract_features.ref_pop_after_first_position import RefPopAfterFirstPosition
from extract_features.session_actions_num_ref_diff_from_impressions import SessionActionNumRefDiffFromImpressions
from extract_features.session_device import SessionDevice
from extract_features.session_filters_active_when_clickout import SessionFilterActiveWhenClickout
from extract_features.session_length import SessionLength
from extract_features.session_num_clickouts import SessionNumClickouts
from extract_features.session_num_filter_sel import SessionNumFilterSel
from extract_features.session_num_inter_item_image import SessionNumInterItemImage
from extract_features.session_num_not_numeric import SessionNumNotNumeric
from extract_features.session_sort_order_when_clickout import SessionSortOrderWhenClickout
from extract_features.statistics_pos_interacted import StatisticsPosInteracted
from extract_features.statistics_time_from_last_action import StatisticsTimeFromLastAction
from extract_features.time_per_impression import TimePerImpression
from extract_features.times_impression_appeared_in_clickouts_session import TimesImpressionAppearedInClickoutsSession
from extract_features.times_user_interacted_with_impression import TimesUserInteractedWithImpression
from extract_features.timing_from_last_interaction_impression import TimingFromLastInteractionImpression
from extract_features.top_pop_interaction_clickout_per_impression import TopPopInteractionClickoutPerImpression
from extract_features.top_pop_interaction_sorting_filters import TopPopInteractionFilters
from extract_features.top_pop_per_impression import TopPopPerImpression
from extract_features.top_pop_sorting_filters import TopPopSortingFilters
from extract_features.user_2_item import User2Item
from extract_features.user_feature import UserFeature
from extract_features.classifier.last_action_before_clickout import LastActionBeforeClickout
from extract_features.session_length_old import SessionLengthOld
from extract_features.user_2_item_old import User2ItemOld
from extract_features.normalized_platform_features_similarity import NormalizedPlatformFeaturesSimilarity
import gc
import utils.menu as menu
from functools import partial
from joblib import Parallel, delayed
import traceback

def create_and_save_feature(mode, cluster, feature_class):
    print(f'creating {str(feature_class)}')
    feature = feature_class(mode=mode, cluster=cluster)
    feature.save_feature(overwrite_if_exists=True)

if __name__ == '__main__':
    features_array = [
       #ActionsInvolvingImpressionSession,
       #ImpressionPositionSession,
       #ImpressionPriceInfoSession,
       #ImpressionRatingNumeric,
       #ImpressionLabel,
       #MeanPriceClickout,
       #AvgPriceInteractions,
       #SessionDevice,
       #NumImpressionsInClickout,
       #SessionLengthOld,
       #TimesImpressionAppearedInClickoutsSession,
       #TimesUserInteractedWithImpression,
       #TimingFromLastInteractionImpression,
       #TopPopPerImpression,
       #TopPopInteractionClickoutPerImpression,
       #ChangeImpressionOrderPositionInSession,
       #FrenzyFactorSession,
       #DayOfWeekAndMomentInDay,
       # LastClickoutFiltersSatisfaction,
       # TimePerImpression,
       # PersonalizedTopPop,
       # PriceQuality,
       # PlatformFeaturesSimilarity,
       # LastActionBeforeClickout,
        # ImpressionStarsNumeric,
         StepsBeforeLastClickout,
        LocationReferencePercentageOfClickouts,
        LocationReferencePercentageOfInteractions,
        NumTimesItemImpressed,
        PercClickPerImpressions,
        PlatformReferencePercentageOfClickouts,
        PlatformReferencePercentageOfInteractions,
        PlatformSession,
        User2ItemOld,
        LazyUser,
        NormalizedPlatformFeaturesSimilarity,
      # PastFutureSessionFeatures,
        ]

    import multiprocessing as mp
    from utils.menu import yesno_choice

    jobs = int(input('how many jobs?'))
    mp = yesno_choice('do you want mp or not?')

    mode = menu.mode_selection()
    cluster = menu.cluster_selection()

    if mp == 'y':
        Parallel(backend='multiprocessing', n_jobs=jobs, max_nbytes=None)(delayed(create_and_save_feature)
            (
                mode, cluster, f
            ) for f in features_array)
    else:
        for f in features_array:
            try:
                create_and_save_feature(mode, cluster, f)
            except Exception as e:
                print(f" {f.name} throws an exception during feature creation")
                print(e)
                traceback.print_exc()
                continue
