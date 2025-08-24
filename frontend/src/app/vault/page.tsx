'use client';

import { getDays } from "@/api/client";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Calendar, Clock, Play, FileText, Search, Filter } from "lucide-react";
import { useState, useEffect } from "react";
import type { Day } from "@/api/client";

export default function VaultPage() {
  const [days, setDays] = useState<Day[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredDays, setFilteredDays] = useState<Day[]>([]);

  useEffect(() => {
    const fetchDays = async () => {
      try {
        const fetchedDays = await getDays();
        setDays(fetchedDays);
        setFilteredDays(fetchedDays);
      } catch (error) {
        console.error('Failed to fetch days:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDays();
  }, []);

  useEffect(() => {
    if (searchTerm.trim() === '') {
      setFilteredDays(days);
    } else {
      const filtered = days.filter(day => 
        day.summary.toLowerCase().includes(searchTerm.toLowerCase()) ||
        day.date.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setFilteredDays(filtered);
    }
  }, [searchTerm, days]);

  // Sort days by date (newest first)
  const sortedDays = filteredDays.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

  // Format date for display
  const formatDate = (dateString: string) => {
    try {
      const date = new Date(dateString);
      
      // Check if date is valid
      if (isNaN(date.getTime())) {
        return {
          full: 'Invalid Date',
          short: 'Invalid',
          dayOfWeek: 'N/A',
          dayOfMonth: 0
        };
      }
      
      return {
        full: date.toLocaleDateString('en-US', { 
          weekday: 'long', 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric' 
        }),
        short: date.toLocaleDateString('en-US', { 
          month: 'short', 
          day: 'numeric' 
        }),
        dayOfWeek: date.toLocaleDateString('en-US', { weekday: 'short' }),
        dayOfMonth: date.getDate()
      };
    } catch (error) {
      return {
        full: 'Invalid Date',
        short: 'Invalid',
        dayOfWeek: 'N/A',
        dayOfMonth: 0
      };
    }
  };

  // Get day number (assuming this is a survival journey)
  const getDayNumber = (dateString: string) => {
    try {
      // You can customize this logic based on your needs
      const startDate = new Date('2024-01-01'); // Adjust this to your start date
      const currentDate = new Date(dateString);
      
      // Check if dates are valid
      if (isNaN(startDate.getTime()) || isNaN(currentDate.getTime())) {
        return 1;
      }
      
      const diffTime = Math.abs(currentDate.getTime() - startDate.getTime());
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      return Math.max(1, diffDays); // Ensure minimum day number is 1
    } catch (error) {
      return 1;
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-background via-background to-muted/20">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center">
            <div className="mx-auto w-24 h-24 bg-muted rounded-full flex items-center justify-center mb-6 animate-pulse">
              <FileText className="w-12 h-12 text-muted-foreground" />
            </div>
            <h1 className="text-4xl font-bold text-foreground mb-4">Loading The Vault...</h1>
            <p className="text-xl text-muted-foreground">
              Retrieving your survival records...
            </p>
          </div>
        </div>
      </div>
    );
  }

  if (days.length === 0) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-background via-background to-muted/20">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center">
            <div className="mx-auto w-24 h-24 bg-muted rounded-full flex items-center justify-center mb-6">
              <FileText className="w-12 h-12 text-muted-foreground" />
            </div>
            <h1 className="text-4xl font-bold text-foreground mb-4">The Vault</h1>
            <p className="text-xl text-muted-foreground mb-8">
              Your journey through the apocalypse awaits...
            </p>
            <div className="bg-card border rounded-lg p-8 max-w-md mx-auto">
              <p className="text-muted-foreground">
                No days have been recorded yet. Check back soon for updates on your survival journey.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-background to-muted/20">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-foreground mb-4">The Vault</h1>
          
          {/* Search and Stats */}
          <div className="max-w-md mx-auto mb-6">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <input
                type="text"
                placeholder="Search days or summaries..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 bg-card border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all"
              />
            </div>
          </div>
          
          <div className="flex items-center justify-center gap-4 flex-wrap">
            <Badge variant="secondary" className="text-sm">
              <Calendar className="w-4 h-4 mr-2" />
              {filteredDays.length} of {days.length} Days
            </Badge>
            <Badge variant="outline" className="text-sm">
              <Clock className="w-4 h-4 mr-2" />
              Latest: {sortedDays.length > 0 ? formatDate(sortedDays[0].date).short : 'N/A'}
            </Badge>
          </div>
        </div>

        {/* Days Grid */}
        {filteredDays.length === 0 ? (
          <div className="text-center py-12">
            <div className="bg-card border rounded-lg p-8 max-w-md mx-auto">
              <Search className="w-12 h-12 mx-auto mb-4 text-muted-foreground opacity-50" />
              <h3 className="text-lg font-semibold text-foreground mb-2">No Results Found</h3>
              <p className="text-muted-foreground">
                Try adjusting your search terms or browse all days.
              </p>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {sortedDays.map((day, index) => {
              const dateInfo = formatDate(day.date);
              const dayNumber = getDayNumber(day.date);
              
              return (
                <Card key={day.date} className="group hover:shadow-lg transition-all duration-300 hover:-translate-y-1 border-2 hover:border-primary/20">
                  <CardHeader className="pb-4">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-3 mb-2">
                          <Badge variant="default" className="text-xs">
                            Day {dayNumber}
                          </Badge>
                          <Badge variant="outline" className="text-xs">
                            {dateInfo.dayOfWeek}
                          </Badge>
                        </div>
                        <CardTitle className="text-lg font-semibold text-foreground">
                          {dateInfo.full}
                        </CardTitle>
                      </div>
                      <div className="text-right">
                        <div className="text-2xl font-bold text-primary">
                          {dateInfo.dayOfMonth}
                        </div>
                        <div className="text-xs text-muted-foreground uppercase tracking-wide">
                          {dateInfo.short}
                        </div>
                      </div>
                    </div>
                  </CardHeader>
                  
                  <CardContent className="space-y-4">
                    {/* Summary */}
                    <div className="space-y-2">
                      <h4 className="font-medium text-sm text-muted-foreground uppercase tracking-wide">
                        Daily Summary
                      </h4>
                      <p className="text-sm text-foreground leading-relaxed">
                        {day.summary.length > 150 
                          ? `${day.summary.substring(0, 150)}...` 
                          : day.summary
                        }
                      </p>
                    </div>

                    {/* Video Section */}
                    <div className="space-y-2">
                      <h4 className="font-medium text-sm text-muted-foreground uppercase tracking-wide flex items-center gap-2">
                        <Play className="w-4 h-4" />
                        Video Record
                      </h4>
                      <div className="relative group/video">
                        {day.video_url ? (
                          <video 
                            src={day.video_url} 
                            controls 
                            className="w-full rounded-lg border bg-muted/50 hover:bg-muted/70 transition-colors"
                            preload="metadata"
                            onError={(e) => {
                              console.error('Video failed to load:', day.video_url);
                            }}
                          />
                        ) : (
                          <div className="w-full h-32 bg-muted/50 rounded-lg border flex items-center justify-center">
                            <div className="text-center text-muted-foreground">
                              <Play className="w-8 h-8 mx-auto mb-2 opacity-50" />
                              <p className="text-xs">No video available</p>
                            </div>
                          </div>
                        )}
                        <div className="absolute inset-0 bg-black/0 group-hover/video:bg-black/10 transition-colors rounded-lg pointer-events-none" />
                      </div>
                    </div>

                    {/* Quick Stats */}
                    <div className="pt-2 border-t border-border/50">
                      <div className="flex items-center justify-between text-xs text-muted-foreground">
                        <span>Record #{index + 1}</span>
                        <span>•</span>
                        <span>{day.date}</span>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        )}

        {/* Footer */}
        {/* <div className="mt-16 text-center">
          <div className="bg-card border rounded-lg p-6 max-w-2xl mx-auto">
            <h3 className="text-lg font-semibold text-foreground mb-2">
              The Journey Continues...
            </h3>
            <p className="text-muted-foreground">
              Each entry in this vault represents a day of survival, a story of resilience, 
              and a testament to humanity's will to endure. Keep checking back for new chapters 
              in your apocalyptic journey.
            </p>
          </div>
        </div> */}
      </div>
    </div>
  );
}
