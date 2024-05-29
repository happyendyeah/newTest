public class test {
	public void add(TimeSeriesDataItem item, boolean notify) {
		if (!(item == null))
			;
		else {
			throw new IllegalArgumentException("Null 'item' argument.");
		}
		findBoundsByIteration();
		item = (TimeSeriesDataItem) item.clone();
		Class c = item.getPeriod().getClass();
		if (!(this.timePeriodClass == null)) {
			if (!this.timePeriodClass.equals(c)) {
				StringBuffer b = new StringBuffer();
				b.append("You are trying to add data where the time period class ");
				b.append("is ");
				b.append(item.getPeriod().getClass().getName());
				b.append(", but the TimeSeries is expecting an instance of ");
				b.append(this.timePeriodClass.getName());
				b.append(".");
				throw new SeriesException(b.toString());
			}
		} else {
			this.timePeriodClass = c;
		}

		// make the change (if it's not a duplicate time period)...
		boolean added = false;
		int count = getItemCount();
		if (!(count == 0)) {
			RegularTimePeriod last = getTimePeriod(getItemCount() - 1);
			if (item.getPeriod().compareTo(last) > 0) {
				this.data.add(item);
				added = true;
			} else {
				int index = Collections.binarySearch(this.data, item);
				if (index < 0) {
					this.data.add(-index - 1, item);
					added = true;
				} else {
					StringBuffer b = new StringBuffer();
					b.append("You are attempting to add an observation for ");
					b.append("the time period ");
					b.append(item.getPeriod().toString());
					b.append(" but the series already contains an observation");
					b.append(" for that time period. Duplicates are not ");
					b.append("permitted.  Try using the addOrUpdate() method.");
					throw new SeriesException(b.toString());
				}
			}
		} else {
			this.data.add(item);
			added = true;
		}
		if (!(added))
			;
		else {
			updateBoundsForAddedItem(item);
			if (getItemCount() > this.maximumItemCount) {
				TimeSeriesDataItem d = (TimeSeriesDataItem) this.data.remove(0);
				updateBoundsForRemovedItem(d);
			}
			removeAgedItems(false);
			if (notify) {
				fireSeriesChanged();
			}
		}

	}
}