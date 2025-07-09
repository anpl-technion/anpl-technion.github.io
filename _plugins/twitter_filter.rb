module Jekyll
  module TwitterFilter
    def linkify_tweet(input, urls)
      return input if urls.nil? || urls.empty?
      
      result = input
      urls.each do |url|
        # Replace t.co URLs with clickable links
        result = result.gsub(url['url'], "<a href=\"#{url['expanded_url']}\" target=\"_blank\">#{url['display_url']}</a>")
      end
      
      result
    end
  end
end

Liquid::Template.register_filter(Jekyll::TwitterFilter)