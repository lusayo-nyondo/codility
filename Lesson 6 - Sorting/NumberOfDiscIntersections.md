We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

content_copy


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)
content_copy

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Copyright 2009–2026 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

===================

ere is a concise breakdown of the Disc Intersections algorithm for your notes. Think of it as a "Timeline" or "Sweep-line" problem.1. The TransformationWe convert each disc into a 1D interval on the x-axis:Left Point = $Center - Radius$Right Point = $Center + Radius$2. The Sorting StrategyWe don't care which left point belongs to which right point. We create two independent sorted lists: left_boundaries and right_boundaries.Sorting allows us to "walk" across the x-axis and process events (discs starting or ending) in order.3. The "People in a Room" AnalogyImagine the x-axis is time and the discs are guests at a bar:Left Boundary: A guest enters the room.Right Boundary: A guest leaves the room.Intersection: When a guest enters, they must "clink glasses" (intersect) with everyone already in the room.4. The Sweep-Line ProcessWe loop through every left_pt in our sorted left_boundaries.Check Departures: Before the current disc "enters," we check right_boundaries. If any right boundary is less than our current left_pt, that disc has already "left." We decrement our active_discs count.Count Intersections: The new disc intersects with all active_discs currently in the room. We add this count to our total.Update State: We increment active_discs because the current disc is now "in the room" for the next one to meet.ComplexityTime: $O(N \log N)$ because of the sorting. The actual sweep is $O(N)$.Space: $O(N)$ to store the boundary arrays.