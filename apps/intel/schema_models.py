
from django.db import models
from datetime import datetime, timedelta

class IntelGrameenSafeMotherhoodFollowup(models.Model):
    form_id = models.IntegerField()
    # id = models.IntegerField()
    meta_deviceid = models.CharField(max_length=765, blank=True)
    meta_timestart = models.DateTimeField(null=True, blank=True)
    meta_timeend = models.DateTimeField(null=True, blank=True)
    meta_username = models.CharField(max_length=765, blank=True)
    safe_pregnancy_meta_chw_id = models.CharField(max_length=765, blank=True)
    meta_uid = models.CharField(max_length=765, blank=True)
    meta_commcareversion = models.CharField(max_length=765, blank=True)
    safe_pregnancy_case_case_id = models.CharField(max_length=765, blank=True)
    safe_pregnancy_case_date_modified = models.CharField(max_length=19, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_bednet = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_iron_folic = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_vitamin_a = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_start_tt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_finish_tt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_start_ipt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_finish_ipt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_deworm = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_birth_plan = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_update_pregnancy_actions_test_syphilis = models.CharField(max_length=4, blank=True)
    safe_pregnancy_case_referral_referral_id = models.CharField(max_length=765, blank=True)
    safe_pregnancy_case_referral_followup_date = models.CharField(max_length=10, blank=True)
    safe_pregnancy_case_referral_open_referral_types = models.CharField(max_length=765, blank=True)
    safe_pregnancy_feeling = models.CharField(max_length=765, blank=True)
    safe_pregnancy_pain_from_vagina = models.CharField(max_length=765, blank=True)
    safe_pregnancy_headache_or_b_vision = models.CharField(max_length=765, blank=True)
    safe_pregnancy_dark_urine = models.CharField(max_length=765, blank=True)
    safe_pregnancy_poor_night_vision = models.CharField(max_length=765, blank=True)
    safe_pregnancy_swelling = models.CharField(max_length=765, blank=True)
    safe_pregnancy_unusual_pain = models.CharField(max_length=765, blank=True)
    safe_pregnancy_burn_urinate = models.CharField(max_length=765, blank=True)
    safe_pregnancy_baby_movement = models.CharField(max_length=765, blank=True)
    safe_pregnancy_baby_not_moving = models.CharField(max_length=765, blank=True)
    safe_pregnancy_fever = models.CharField(max_length=765, blank=True)
    safe_pregnancy_other_illness = models.CharField(max_length=765, blank=True)
    safe_pregnancy_which_illness = models.CharField(max_length=765, blank=True)
    safe_pregnancy_referred = models.CharField(max_length=765, blank=True)
    safe_pregnancy_referral_id = models.CharField(max_length=765, blank=True)
    safe_pregnancy_referral = models.CharField(max_length=765, blank=True)
    safe_pregnancy_preg_actions = models.CharField(max_length=765, blank=True)
    safe_pregnancy_smoking = models.CharField(max_length=765, blank=True)
    safe_pregnancy_counsel_smoking = models.CharField(max_length=765, blank=True)
    safe_pregnancy_food = models.CharField(max_length=765, blank=True)
    safe_pregnancy_answer_food = models.CharField(max_length=765, blank=True)
    safe_pregnancy_umbilical_cord = models.CharField(max_length=765, blank=True)
    safe_pregnancy_answer_umbilical_cord = models.CharField(max_length=765, blank=True)
    safe_pregnancy_newborns = models.CharField(max_length=765, blank=True)
    safe_pregnancy_answer_newborns = models.CharField(max_length=765, blank=True)
    safe_pregnancy_breast_feed = models.CharField(max_length=765, blank=True)
    safe_pregnancy_answer_breast_feed = models.CharField(max_length=765, blank=True)
    safe_pregnancy_thank_you = models.CharField(max_length=765, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    meta_formname = models.CharField(max_length=765, blank=True)
    meta_formversion = models.CharField(max_length=765, blank=True)
    safe_pregnancy_meta_userid = models.CharField(max_length=765, blank=True)
    safe_pregnancy_case_id = models.CharField(max_length=765, blank=True)
    safe_pregnancy_preg_actions_bednet = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_iron_folic = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_vitamin_a = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_start_tt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_finish_tt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_start_ipt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_finish_ipt = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_deworm = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_birth_plan = models.CharField(max_length=4, blank=True)
    safe_pregnancy_preg_actions_test_syphilis = models.CharField(max_length=4, blank=True)
    class Meta:
        db_table = u'view_intel_grameen_safe_motherhood_followups'

    @property
    def visit_date(self):
        # for conveniece / clarity
        return self.meta_timestart

class IntelGrameenMotherRegistration(models.Model):
    form_id = models.IntegerField()
    # id = models.IntegerField()
    meta_deviceid = models.CharField(max_length=765, blank=True)
    meta_timestart = models.DateTimeField(null=True, blank=True)
    meta_timeend = models.DateTimeField(null=True, blank=True)
    meta_username = models.CharField(max_length=765, blank=True)
    meta_uid = models.CharField(max_length=765, blank=True)
    sampledata_meta_chw_id = models.CharField(max_length=765, blank=True)
    meta_commcareversion = models.CharField(max_length=765, blank=True)
    sampledata_case_case_id = models.CharField(max_length=765, blank=True)
    sampledata_case_date_modified = models.CharField(max_length=19, blank=True)
    sampledata_case_create_case_type_id = models.CharField(max_length=765, blank=True)
    sampledata_case_create_user_id = models.CharField(max_length=765, blank=True)
    sampledata_case_create_case_name = models.CharField(max_length=765, blank=True)
    sampledata_case_create_external_id = models.CharField(max_length=765, blank=True)
    sampledata_case_update_prp_edk = models.CharField(max_length=10, blank=True)
    sampledata_case_update_prp_hrk = models.CharField(max_length=4, blank=True)
    sampledata_household = models.IntegerField(null=True, blank=True)
    sampledata_case_id = models.IntegerField(null=True, blank=True)
    sampledata_address = models.CharField(max_length=765, blank=True)
    sampledata_phone = models.CharField(max_length=11, blank=True)
    sampledata_mother_name = models.CharField(max_length=765, blank=True)
    sampledata_mother_age = models.IntegerField(null=True, blank=True)
    sampledata_mother_height = models.CharField(max_length=765, blank=True)
    sampledata_partner_name = models.CharField(max_length=765, blank=True)
    sampledata_partner_occupation = models.CharField(max_length=765, blank=True)
    sampledata_weeks_pregnant = models.IntegerField(null=True, blank=True)
    sampledata_previous_pregnancies = models.IntegerField(null=True, blank=True)
    sampledata_previous_deliveries = models.IntegerField(null=True, blank=True)
    sampledata_previous_terminations = models.IntegerField(null=True, blank=True)
    sampledata_previous_newborn_death = models.CharField(max_length=765, blank=True)
    sampledata_over_5_years = models.CharField(max_length=765, blank=True)
    sampledata_previous_csection = models.CharField(max_length=765, blank=True)
    sampledata_previous_bleeding = models.CharField(max_length=765, blank=True)
    sampledata_heart_problems = models.CharField(max_length=765, blank=True)
    sampledata_diabetes = models.CharField(max_length=765, blank=True)
    sampledata_hip_problems = models.CharField(max_length=765, blank=True)
    sampledata_result_card_present = models.CharField(max_length=765, blank=True)
    sampledata_result_card_willing = models.CharField(max_length=765, blank=True)
    sampledata_result_card_get = models.CharField(max_length=765, blank=True)
    sampledata_card_results_syphilis_test = models.CharField(max_length=765, blank=True)
    sampledata_card_results_syphilis_result = models.CharField(max_length=765, blank=True)
    sampledata_card_results_get_tested_info_syphilis = models.CharField(max_length=765, blank=True)
    sampledata_card_results_blood_group_known = models.CharField(max_length=765, blank=True)
    sampledata_card_results_get_tested_info_blood_group = models.CharField(max_length=765, blank=True)
    sampledata_card_results_blood_group = models.CharField(max_length=765, blank=True)
    sampledata_card_results_hepb_test = models.CharField(max_length=765, blank=True)
    sampledata_card_results_get_tested_info_hepb = models.CharField(max_length=765, blank=True)
    sampledata_card_results_hepb_result = models.CharField(max_length=765, blank=True)
    sampledata_card_results_hb_test_known = models.CharField(max_length=765, blank=True)
    sampledata_card_results_get_tested_info_hb_test = models.CharField(max_length=765, blank=True)
    sampledata_card_results_hb_test = models.CharField(max_length=765, blank=True)
    sampledata_more_details = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_old = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_young = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_small = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_5_years = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_complications = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_many = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_health = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_blood_group = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_syphilis = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_hepb = models.CharField(max_length=765, blank=True)
    sampledata_hi_risk_info_anemia = models.CharField(max_length=765, blank=True)
    sampledata_too_late = models.CharField(max_length=765, blank=True)
    sampledata_continue = models.CharField(max_length=765, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    sampledata_case_referral_referral_id = models.CharField(max_length=765, blank=True)
    sampledata_case_referral_followup_date = models.CharField(max_length=10, blank=True)
    sampledata_case_referral_open_referral_types = models.CharField(max_length=765, blank=True)
    sampledata_duplicate = models.CharField(max_length=765, blank=True)
    sampledata_phone_2 = models.CharField(max_length=765, blank=True)
    meta_formname = models.CharField(max_length=765, blank=True)
    meta_formversion = models.CharField(max_length=765, blank=True)
    sampledata_meta_userid = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'view_intel_grameen_safe_motherhood_registrations'

    @property
    def months_pregnant(self):
        """
        Dynamically calculate months pregnant based on the visit date 
        and how far in they were at that point
        """
        additional_time = datetime.now() - self.meta_timestart
        total_days = self.sampledata_weeks_pregnant * 7 + additional_time.days
        return total_days / 30
    
    @property
    def registration_date(self):
        # for conveniece / clarity
        return self.meta_timestart
    
    @property 
    def pregnancy_start_date(self):
        # guess the LMP
        return self.registration_date - timedelta(days=7*self.sampledata_weeks_pregnant)
        
    @property
    def pregnancy_due_date(self):
        # EDD ~= LMP + 40 weeks
        return self.pregnancy_start_date + timedelta(days=7*40)