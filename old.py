    def test_auto_complete_on_searchbar(self):
        self.youtube_page = Youtube_page("http://www.youtube.com")
        self.youtube_page.search_autocomplete_flow("Python Prog")
        self.current_title = self.youtube_page.get_page_title()
        self.assertIn("python programming",self.current_title)
        self.youtube_page.close_page()
 
    def test_empty_search_on_youtube(self):
        self.youtube_page = Youtube_page("http://www.youtube.com")
        self.old_title = self.youtube_page.get_page_title()
        self.youtube_page.search_flow("")
        self.current_title = self.youtube_page.get_page_title()
        self.assertEqual(self.old_title,self.current_title)
        self.youtube_page.close_page()

    def test_search_on_youtube(self):
        self.youtube_page = Youtube_page("http://www.youtube.com")
        self.youtube_page.search_flow("Python Programming")
        self.current_title = self.youtube_page.get_page_title()
        self.assertIn("Python Programming",self.current_title)
        self.youtube_page.close_page()
                   
    def test_change_to_light_theme(self):
        self.youtube_page = Youtube_page("http://www.youtube.com")
        self.youtube_page.click_on_settings()   
        self.youtube_page.click_on_toggle_theme()
        self.youtube_page.toggle_light_theme()
        self.current_theme = self.youtube_page.get_current_page_theme()
        self.assertIn("Light", self.current_theme)
        self.youtube_page.close_page()
        
        
    def test_skip_ad_button(self):
        self.youtube_page = Youtube_page("http://www.youtube.com")
        self.youtube_page.search_flow("Python Programming")
        self.youtube_page.play_random_video_flow()
        self.youtube_page.skip_ad_flow()
        self.assertFalse(self.youtube_page.check_for_ads(),msg = 'The is no AD or Add cannot be skipped')
    